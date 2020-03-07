# -*- coding: utf-8 -*-
__author__ = 'Sky'
import time
from example1_unittest.start_chrome import PythonPrepareTest


class TestV(PythonPrepareTest):
    def testV(self):
        print('start')
        t1 = time.time()
        # time.sleep(3)
        try:
            self.driver.get('https://positronica.ru/')
        except Exception as e:
            print(e)
        t2 = time.time()

        self.driver.save_screenshot('20200229.png')
        print(t2-t1, 'сек')
