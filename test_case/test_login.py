# -*- coding: utf-8 -*-
# @Time    : 2020/12/15 16:53
# @Author  : AiXin
# @Email   : 1454622738@qq.com
from time import sleep
from selenium import webdriver

import pytest

class Test_Login():
    def test_case01(self):
        """直客登录"""
        self.driver.find_element_by_xpath('//a[text() = "登录"]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[1]/div/div/input').send_keys('18273675403')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[2]/div/div/input').send_keys(
            'aixin96177520000')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="pane-login"]/form/div[3]/div/div/input').send_keys('hhr123456')
        sleep(1)
        self.driver.find_element_by_xpath('//span[text() = "登录"]').click()
        sleep(1)
        actual = self.driver.find_element_by_class_name('line_vertical').text
        assert '欢迎 18273675403 来到禾获仁！', actual


if __name__ == '__main__':
    pytest.main()
