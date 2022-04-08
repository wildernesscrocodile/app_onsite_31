# @Time : 2022/3/15 22:22 

# @Author : 麻花

# @File : Comm_Bus.py 

# @Software: PyCharm

from Common.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy as ABY

from Common.logger import MyLog
from PageLocators.login_locators import LoginLocator as loc
from PageLocators.welcome_locators import WelcomeLocator as loc
import time

my_logger = MyLog()

class CommBus(BasePage):

    # 处理APP重置后授予权限
    def do_jurisdiction(self):
        time.sleep(2)
        curAct = self.driver.current_activity
        if curAct.find("ReviewPermissionsActivity") != -1:
            # 点击继续
            self.wait_eleVisible(loc.continue_but)
            self.click_element(loc.continue_but)

    # 处理app第一次打开时同意协议和选择国籍
    def do_welcome(self):
        time.sleep(2)
        # 如果没有找到首页的元素或者当前在BootActivity,那么就是在欢迎页面
        curAct = self.driver.current_activity
        my_logger.info(F"curAct:{curAct}")
        if curAct.find("BootActivity") != -1:
            # 点击同意权限
            self.wait_eleVisible(loc.consent_and_authorization_button)
            self.click_element(loc.consent_and_authorization_button)





