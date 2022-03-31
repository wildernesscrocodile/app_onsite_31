# @Time : 2021/4/6 21:15 

# @Author : 麻花

# @File : meet_list_page.py

# @Software: PyCharm

from Common.basepage import BasePage
from PageLocators.meet_list_locators import MeetListLocator as loc

class MeetList_page(BasePage):

    def get_loginStats(self):
        # 获取当前登录状态，已登录为True,未登录为False
        doc = '判断是否登录成功'
        try:
            self.wait_eleVisible(loc.user_information_avatar_button, doc=doc)
            return True
        except:
            return False

    def click_avatar(self):
        doc = '点击头像'
        self.wait_eleVisible(loc.user_information_avatar_button, doc=doc)
        self.click_element(loc.user_information_avatar_button, doc)


if __name__ == '__main__':
    from PageObjects import login_page
    from appium import webdriver
    pass







