# # @Time : 2021/4/6 13:46
#
# # @Author : 麻花
#
# # @File : conftest.py
#
# # @Software: PyCharm
from Common.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy as ABY
import pytest
import yaml
from  Common.dir_config import caps_dir
from appium import webdriver
#
#
#
@pytest.fixture
def start_app():
    driver = baseDriver()
    do_welcome(driver)


# 处理app第一次打开时同意协议和选择国籍
def do_welcome(driver):
    # 如果没有找到首页的元素或者不包含MainActivity,那么就是在欢迎页面
    curAct = driver.current_activity
    if curAct.find("MainActivity") == -1:
        # 点击同意协议
        BasePage(driver).wait_eleVisible((ABY.ID, 'cn.edu.hust.jwtapp:id/btn_pos'))
        BasePage(driver).click_element((ABY.ID, 'cn.edu.hust.jwtapp:id/btn_pos'))
        # 选择中国人
        BasePage(driver).wait_eleVisible((ABY.ID, 'cn.edu.hust.jwtapp:id/img_1'))
        BasePage(driver).click_element((ABY.ID, 'cn.edu.hust.jwtapp:id/img_1'))
        # 点击我的
        BasePage(driver).wait_eleVisible((ABY.ID, 'cn.edu.hust.jwtapp:id/ll_my'))
        BasePage(driver).click_element((ABY.ID, 'cn.edu.hust.jwtapp:id/ll_my'))


def baseDriver(server_port=4723, noReset=None, automationName=None, **kwargs):

    fs = open(caps_dir + "/caps.yaml")
    desired_caps = yaml.safe_load(fs)

    if noReset is not None:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = automationName

    return webdriver.Remote(f'http://127.0.0.1:{server_port}/wd/hub', desired_caps)
