# @Time : 2020/12/17 15:53

# @Author : 麻花

# @File : demo.py

# @Software: PyCharm
import time

from appium import webdriver
# from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.appiumby import AppiumBy
# adb devices
from PageObjects.login_page import LoginPage
from PageObjects.meet_list_page import MeetList_page
from selenium.webdriver.support.wait import WebDriverWait
from Common.logger import MyLog
import datetime
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy as ABY
from TestDatas import login_datas as LD

desired_caps = {}
# 平台类型
desired_caps["platformName"] = "Android"
# 平台版本号
desired_caps["platformVersion"] = "8"
# 设备名称
desired_caps["deviceName"] = "NFT10-BWFE-8L09575"
# app包名
desired_caps["appPackage"] = "com.huiyi31.signin31"
# app入口activity
# 打开应用首页后，输入下方命令 可得到对应的appActivity
# adb shell dumpsys window w|findstr \/|findstr name=
desired_caps["appActivity"] = "com.huiyi31.signin31.activity.BootActivity"
# desired_caps["appActivity"] = "com.huiyi31.signin31.activity.LoginActivity"
desired_caps['noReset'] = True
# 连接 appium server。前提: appium desktop要启动。有监听端口
# 将 desired_caps发送给 appium server.打开app
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)


LoginPage(driver).login(LD.success_data["user"], LD.success_data["passwd"])

# vvv = MeetList_page(driver).get_loginStats()
# time.sleep(5)
# print(vvv)




