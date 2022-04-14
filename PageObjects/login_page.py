# @Time : 2021/4/6 16:17 

# @Author : 麻花

# @File : login_page.py 

# @Software: PyCharm

from PageLocators.login_locators import LoginLocator as loc
from Common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, passwd):
        doc = "登录页面——登录功能"
        # self.get_element(loc.name_text, doc=doc)
        self.wait_eleVisible(loc.name_text, doc=doc)
        self.input_text(loc.name_text, username, doc)

        self.wait_eleVisible(loc.pwd_text, doc=doc)
        self.input_text(loc.pwd_text, passwd, doc)

        self.click_element(loc.login_but, doc)
