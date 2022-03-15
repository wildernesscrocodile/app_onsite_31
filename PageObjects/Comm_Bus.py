# @Time : 2022/3/15 22:22 

# @Author : 麻花

# @File : Comm_Bus.py 

# @Software: PyCharm

from Common.basepage import BasePage
from appium.webdriver.common.appiumby import AppiumBy as ABY
import time



class CommBus(BasePage):

    # 处理app第一次打开时同意协议和选择国籍
    def do_welcome(self):
        time.sleep(5)
        # 如果没有找到首页的元素或者不包含MainActivity,那么就是在欢迎页面
        curAct = self.driver.current_activity
        if curAct.find("BootActivity") == -1:
            # 点击同意权限
            self.wait_eleVisible((ABY.ID, 'cn.edu.hust.jwtapp:id/btn_pos'))




