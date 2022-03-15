# @Time : 2021/4/6 20:16 

# @Author : 麻花

# @File : test_login.py 

# @Software: PyCharm


import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
# from PageObjects.index_page import IndexPage
# from TestDatas import Common_Datas as CD
from TestDatas import login_datas as LD
from PageObjects.meet_list_page import MeetList_page
# import ddt
import pytest
from Common.logger import MyLog

# @ddt.ddt
my_logger = MyLog()


class TestLogin:

    def setup_class(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8'
        desired_caps['deviceName'] = 'NFT10-BWFE-8L09575'
        desired_caps['appPackage'] = 'com.huiyi31.signin31'
        desired_caps['appActivity'] = 'com.huiyi31.signin31.activity.BootActivity'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['autoGrantPermissions'] = True
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)


    def teardown_class(self):
        pass

    # #   正常用例一登陆成功
    # @pytest.mark.smoke
    # def test_login_2_success(self, access_web):
    #     access_web[1].login(LD.success_data["user"], LD.success_data["passwd"])
    #     # 步骤输入用户名:XXx密码XXX点击登陆
    #     # 断言首页当中一能否找到 退出 这个元素。
    #     assert (MeetList_page(access_web[0]).isExist_logout_ele())

    #   正常用例一登陆成功
    # @pytest.mark.smoke
    def test_login_2_success(self):
        LoginPage(self.driver).login(LD.success_data["user"], LD.success_data["passwd"])
        assert MeetList_page(self.driver).get_loginStats().isExist_logout_ele()




if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "test_login.py"])

    # from PageObjects.login_page import LoginPage
    # from PageObjects.meet_list_page import MeetList_page
    # from appium import webdriver
    #
    # desired_caps = {}
    # # 手机 系统信息
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '8'
    # # 设备号
    # desired_caps['deviceName'] = 'NFT10-BWFE-8L09575'
    # # 包名
    # desired_caps['appPackage'] = 'com.huiyi31.signin31'
    # # 启动名
    # desired_caps['appActivity'] = 'com.huiyi31.signin31.activity.BootActivity'
    # desired_caps['automationName'] = 'Uiautomator2'
    # # 允许输入中文
    # desired_caps['unicodeKeyboard'] = True
    # desired_caps['resetKeyboard'] = True
    # desired_caps['autoGrantPermissions'] = True
    # desired_caps['noReset'] = True
    # # 手机驱动对象
    # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    #
    # sss = LoginPage(driver)
    # sss.login("14311233333", "huiyi@31")
    # # WebDriverWait(sss, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@title="智能学习助手后端"]')))
    # # MeetList_page(sss)
    # ccc = MeetList_page(driver)
