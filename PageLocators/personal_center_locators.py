#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: personal_center_locators.py
# @Author: ---
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 3月 25, 2022
# ---

from appium.webdriver.common.appiumby import AppiumBy as ABY

class PersonalCenter_locatorsLocator:

    #   退出登录按钮
    logout_button = (ABY.LINK_TEXT, '退出登录')


