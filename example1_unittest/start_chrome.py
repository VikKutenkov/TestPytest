# coding: utf-8
__author__ = 'Sky'

import unittest
from selenium import webdriver

class PythonPrepareTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('--ignore-certificate-errors ')
        options.add_argument('--headless')  # отключить визуализацию открытия браузера

        self.driver = webdriver.Chrome(options=options, executable_path='../chromedriver.exe')

        self.driver.set_page_load_timeout(400)
        self.driver.implicitly_wait(4)
        self.driver.set_window_size(1280, 720)  # Не менять! Все тесты заточены под этот размер браузера!
        self.driver.set_script_timeout(4)
        print('SetUp Chrome')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
