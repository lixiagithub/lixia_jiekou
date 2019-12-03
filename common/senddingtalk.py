import requests
import json
def sendmessage(cont):
    message={

    "msgtype": "text",
    "text": {
    "content": cont
   }
    }
    url="自己的钉钉url"

    headers = {
    'Content-Type': 'application/json'

    }
    requests.post(url=url,data=json.dumps(message),headers=headers)

if  __name__=="__main__":
    sendmessage("测试报告")