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
from Common.commons import *


class MeetListLocator:
    appPackag = get_appPackage()


    #   用户信息头像按钮
    user_information_avatar_button = (ABY.ID, f'{appPackag}:id/hy_liebiao_people')

    #   列表页搜索按钮
    list_search_button = (ABY.ID, f'{appPackag}:id/hy_liebiao_search')

    #   搜索文本框
    search_textbox = (ABY.ID, f'{appPackag}:id/hy_et_search')

    #   搜索结果页搜索按钮
    search_button = (ABY.ID, f'{appPackag}:id/hy_search_btn')

    # 搜索会议结果页的会议名称
    search_page_conferencename = (ABY.ANDROID_UIAUTOMATOR, 'new UiSelector().text("礼智信")')
