#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: meet_list_locators.py
# @Author: ---
# @Institution: --- University, ---, China
# @E-mail: ---@---.com, ---@---.edu.cn
# @Site: 
# @Time: 3月 25, 2022
# ---

from appium.webdriver.common.appiumby import AppiumBy as ABY

class MeetListLocator:

    #   用户信息头像按钮
    user_information_avatar_button = (ABY.ID, 'com.huiyi31.signin31.debug:id/hy_liebiao_people')