# coding:utf-8
import unittest


class Test1(unittest.TestCase):

    def setUp(self):
        print("start!")

    def tearDown(self):
        print("end!")

    def test_01(self):
        a = 1
        b = 2
        self.assertTrue(3, a+b)

    def test_02(self):
        a = 3
        b = 2
        self.assertTrue(6, a*b)

if __name__ == "__main__":
    unittest.main()
