# coding: utf-8
__author__ = 'Sky'
from selenium import webdriver
import pytest
import time

@pytest.fixture()
def test_setup_chrome():
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors ')
    # options.add_argument('--headless')  # отключить визуализацию открытия браузера
    driver = webdriver.Chrome(options=options, executable_path=r'F:/VikProject/pytest/20200219_vikpy/drivers/chromedriver.exe')
    driver.set_page_load_timeout(400)
    driver.implicitly_wait(4)
    driver.set_window_size(1280, 720)  # Не менять! Все тесты заточены под этот размер браузера!
    driver.set_script_timeout(4)
    print('SetUp Chrome')
    yield
    driver.close()
    driver.quit()
    print('TearDown Chrome')


def test_20200302(test_setup_chrome):
    t1 = time.time()
    try:
        driver.get('https://positronica.ru/')
    except Exception as e:
        print(e)
    t2 = time.time()

    driver.save_screenshot(str(int(t2))+'.png')
    print(t2-t1, 'сек')

    x = 0
    assert(x == 0)
    print('test_20200302 end')


# def test_end():
#     # driver.close()
#     driver.quit()
#     print('TearDown Chrome')
