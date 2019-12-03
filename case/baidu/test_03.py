import requests
import unittest
import HTMLTestRunnerCN
from config import baseurl
from common import readtxt
import ddt
restlue=readtxt.get()
#url = baseurl + restlue[0]['url']
@ddt.ddt
class Testcase(unittest.TestCase):
    def tearDown(self) -> None:
        pass
    def setUp(self) -> None:
        pass
    @ddt.data(*restlue)
    def testone(self):

        url=baseurl+restlue['url']
        response = requests.request(restlue['method'], url, data=restlue['data'], headers=eval(restlue['headers']))

        self.assertTrue(restlue['assert'] in response.text)

    # def testtwo(self):
    #     response = requests.request(restlue[1]['method'], url, data=restlue[1]['data'],headers=eval(restlue[1]['headers']))
    #
    #     self.assertTrue(restlue[1]['assert'] in response.text)
if __name__=="__main__":
    import os
    suit = unittest.TestSuite()
    loader = unittest.TestLoader()
    suit.addTests(loader.discover(os.getcwd()))
    filePath = 'report.html'
    fp = open(filePath, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='Test Report',
        description='Test Report'
    )
    runner.run(suit)
    fp.close()