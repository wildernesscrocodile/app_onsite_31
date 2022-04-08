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
from Common.dir_config import caps_dir
from appium import webdriver
from PageObjects.Comm_Bus import CommBus
from PageObjects.meet_list_page import MeetList_page
from PageObjects.personal_center_page import PersonalCenterPage



#
#
#

@pytest.fixture
def start_app(request):
    param = request.param
    driver = baseDriver(noReset=param["noReset"])
    # 授予权限
    CommBus(driver).do_jurisdiction()
    # 处理欢迎页面
    CommBus(driver).do_welcome()
    # 1.判断当前用户是否已登录
    if MeetList_page(driver).get_loginStats():
        # 点击头像，再点击退出登录
        MeetList_page(driver).click_avatar()
        # 2、如果已登录，先退出
        PersonalCenterPage(driver).logout()

    yield driver


def baseDriver(server_port=4723, noReset=None, automationName=None, **kwargs):
    fs = open(caps_dir + "/caps.yaml")
    desired_caps = yaml.safe_load(fs)

    if noReset is not None:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = automationName

    return webdriver.Remote(f'http://127.0.0.1:{server_port}/wd/hub', desired_caps)
