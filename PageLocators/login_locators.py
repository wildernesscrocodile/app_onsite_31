# @Time : 2021/4/6 16:18 

# @Author : 麻花

# @File : login_locators.py 

# @Software: PyCharm

from appium.webdriver.common.appiumby import AppiumBy as ABY

class LoginLocator:
    name_text = (ABY.ID, 'com.huiyi31.signin31.debug:id/hy_login_name')
    pwd_text = (ABY.ID, 'com.huiyi31.signin31.debug:id/hy_login_pwd')
    login_but = (ABY.ID, 'com.huiyi31.signin31.debug:id/hy_login_bt')

