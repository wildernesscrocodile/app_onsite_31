#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: welcome_locators.py
# @Author: ---
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 3月 25, 2022
# ---

from appium.webdriver.common.appiumby import AppiumBy as ABY

class WelcomeLocator:

    # 授予权限页面——继续按钮
    continue_but = (ABY.ID, 'com.android.packageinstaller:id/continue_button')

    #   同意并授权按钮
    consent_and_authorization_button = (ABY.ID, 'com.huiyi31.signin31.debug:id/sure')

