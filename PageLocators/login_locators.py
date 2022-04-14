# @Time : 2021/4/6 16:18 

# @Author : 麻花

# @File : login_locators.py 

# @Software: PyCharm

from appium.webdriver.common.appiumby import AppiumBy as ABY
from Common.commons import *

class LoginLocator:
    appPackag = get_appPackage()

    name_text = (ABY.ID, f'{appPackag}:id/hy_login_name')
    pwd_text = (ABY.ID, f'{appPackag}:id/hy_login_pwd')
    login_but = (ABY.ID, f'{appPackag}:id/hy_login_bt')

