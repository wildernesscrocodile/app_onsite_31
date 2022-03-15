# @Time : 2021/4/6 16:17 

# @Author : 麻花

# @File : login_page.py 

# @Software: PyCharm

from PageLocators.login_locators import LoginLocator as loc
from Common.basepage import BasePage
from appium import webdriver

# def init_driver():
#     desired_caps = {}
#     # 手机 系统信息
#     desired_caps['platformName'] = 'Android'
#     desired_caps['platformVersion'] = '8'
#     # 设备号
#     desired_caps['deviceName'] = 'NFT10-BWFE-8L09575'
#     # 包名
#     desired_caps['appPackage'] = 'com.huiyi31.signin31'
#     # 启动名
#     desired_caps['appActivity'] = 'com.huiyi31.signin31.activity.BootActivity'
#     desired_caps['automationName'] = 'Uiautomator2'
#     # 允许输入中文
#     desired_caps['unicodeKeyboard'] = True
#     desired_caps['resetKeyboard'] = True
#     desired_caps['autoGrantPermissions'] = True
#     desired_caps['noReset'] = True
#     # 手机驱动对象
#     driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
#     return driver


class LoginPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    def login(self, username, passwd):
        doc = "登录页面——登录功能"
        # self.get_element(loc.name_text, doc=doc)
        self.wait_eleVisible(loc.name_text, doc=doc)
        self.input_text(loc.name_text, username, doc)

        self.wait_eleVisible(loc.pwd_text, doc=doc)
        self.input_text(loc.pwd_text, passwd, doc)

        self.click_element(loc.login_but, doc)
