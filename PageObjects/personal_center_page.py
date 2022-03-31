#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: personal_center_page.py
# @Author: ---
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 3月 25, 2022
# ---
from PageLocators.personal_center_locators import PersonalCenter_locatorsLocator as loc
from Common.basepage import BasePage


class PersonalCenterPage(BasePage):

    def logout(self):
        doc = "个人中心页面——退出登录功能"
        self.wait_eleVisible(loc.logout_button, doc=doc)
        self.click_element(loc.logout_button, doc)







