# @Time : 2021/4/6 21:15 

# @Author : 麻花

# @File : meet_list_page.py

# @Software: PyCharm

from Common.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy as ABY
from selenium.webdriver.support.wait import WebDriverWait



class MeetList_page(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def get_loginStats(self):
        # 获取当前登录状态，已登录为True,未登录为False
        try:
            BasePage(self).wait_eleVisible((ABY.ID, 'com.huiyi31.signin31:id/hy_liebiao_people'))
            return False
        except:
            return True

    # def get_loginStats(self):
    #     doc = '判断是否登录成功'
    #     try:
    #         self.wait_eleVisible(((ABY.ID, 'com.huiyi31.signin31:id/hy_liebiao_people')), doc=doc)
    #         return False
    #     except:
    #         return True


if __name__ == '__main__':
    from PageObjects import login_page
    from appium import webdriver
    pass







