# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 16:54
# @Author  : AiXin
# @Email   : 1454622738@qq.com

import pytest
from selenium import webdriver


def __init__(self):
    self.driver = webdriver.Chrome('../driver/chromedriver.exe')


@pytest.fixture(scope='function', autouse=True)
def setup(self):
    self.driver.get('http://test.hhrchina.com/')
    self.driver.maximize_window()
    self.driver.find_element_by_class_name('close-img').click()
    self.driver.implicitly_wait(10)
    yield
    self.driver.quit()
