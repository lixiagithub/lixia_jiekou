# coding:utf-8
import os
import unittest
import time
import HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 当前脚本所在文件真实路径
cur_path = os.path.dirname(os.path.realpath(__file__))


def add_case(case_name="case", rule="test*.py"):
    """第一步：加载所有测试用例"""
    # 连接目录与文件名或目录=用例文件夹
    case_path = os.path.join(cur_path, case_name)
    # 如果不存在这个case文件夹，就自动创建一个
    if not os.path.exists(case_path):
        os.mkdir(case_path)
    print("test case path:%s" % case_path)
    # 定义discover方法的参数,defaultTestLoader()类，通过该类下面的discover()方法可自动根据测试目录start_dir
    # 匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    print(discover)
    return discover


def run_case(all_case, report_name="report"):
    """第二步：执行所有用例，并把结果写入HTML测试报告"""
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    # 连接目录与文件名或目录=报告文件夹
    report_path = os.path.join(cur_path, report_name)
    # 如果不存在这个report文件夹，就自动创建一个
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    report_abspath = os.path.join(report_path, now+"result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告，测试结果如下：',
                                           description=u'用例执行情况：')
    # 调用add_case函数返回值,通过run()方法执行discover
    runner.run(all_case)
    fp.close()


def get_report_file(report_path):
    """第三步：获取最新测试报告
    1.如果第二步生成的测试报告加了时间戳，想找到最新的文件就用第三步
    2.如果第二步不加时间戳，只是生成result.html，那这一步其实没卵用，可以忽略"""
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新生成的测试报告：'+lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(report_path, lists[-1])
    return report_file


def send_mail(sender, psw, receiver, smtp_server, report_file, port):
    """第四步：发送最新的测试报告内容
    1.像QQ邮箱这种ssl加密的就走SMTP_SSL，用授权码登录
    2.其它邮箱就正常账号密码登录，走SMTP"""
    with open(report_file, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = psw
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtp_server, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtp_server, port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('test report email has send out')


if __name__ == "__main__":
    all_case = add_case()  # 1加载用例
    # 生成测试报告路径
    run_case(all_case)  # 2执行用例
    # 获取最新的测试报告文件
    report_path = os.path.join(cur_path, "report")
    report_file = get_report_file(report_path)  # 3获取最新测试报告
    # 邮箱配置
    from config import ReadConfig
    sender = ReadConfig.sender
    psw = ReadConfig.psw
    smtp_server = ReadConfig.smtp_server
    port = ReadConfig.port
    receiver = ReadConfig.receiver
    send_mail(sender, psw, receiver, smtp_server, report_file, port)  # 4最后一步发送报告

