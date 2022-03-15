# @Time : 2021/4/6 13:46 

# @Author : 麻花

# @File : basepage.py 

# @Software: PyCharm


from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import datetime
import time
from Common import dir_config
from selenium.webdriver.common.keys import Keys
from Common.logger import MyLog
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement


from selenium.webdriver.remote.webelement import WebElement

# 封装基本函数  执行日志.

my_logger = MyLog()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, times=30, poll_frequency=0.5, doc=""):
        '''

        :param locator:
        :param times:
        :param poll_frequency:
        :param doc:
        :return:
        '''
        my_logger.info("等待元素{0}可见".format(locator))
        try:
            # 开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间点
            end = datetime.datetime.now()
            # 求一个差值，写在日志当中。等待了多久。
            Difference = (end - start).seconds
            my_logger.info("等待结束。等待时长为:{0}秒".format(Difference))
        except:
            my_logger.error("等待元素可见失败!!!")
            self.save_screenshot(doc)
            raise

    # 等待元素存在
    def wait_elePresence(self):

        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        my_logger.info("{0},查找元素: {1}".format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            my_logger.error("查找元素失败! ! ! ")
            # 截图
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 点击操作
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        my_logger.info("{0}点击元素:{1}".format(doc, locator))
        try:
            ele.click()
        except:
            my_logger.error("元素点击操作失败! ! ! ")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        my_logger.info("{0}:元素：{1}输入内容：{2}".format(doc, locator, text))
        # 输入操作
        try:
            ele.send_keys(text)
            my_logger.info("{0}输入成功:{1}".format(doc, locator))
        except:
            my_logger.error("元素输入操作失败! ! ! ")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        ele = self.get_element(locator, doc)
        # 元素操作
        my_logger.info("{0}获取元素：文本内容:{1}".format(doc, locator))
        try:
            text = ele.text
            my_logger.info("元素{0}的文本内容为：{1}".format(locator, text))
            return text
        except:
            my_logger.error("获取元素文本内容失败! ! ! ")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_elment_attribute(self, locator, attr, doc=""):
        ele = self.get_element(locator, doc)
        my_logger.info("{0}输入成功:{1}".format(doc, locator))
        # 元素操作
        try:
            ele_attr = ele.get_attribute(attr)
            my_logger.info("元素{0}的属性{1}值为：{2}".format(locator, attr, ele_attr))
            return ele_attr
        except:
            my_logger.error("获取元素属性失败! ! ! ")
            # 截图
            self.save_screenshot(doc)
            raise

    # 元素存在未Ture,否则为False
    def is_eleExist(self, locator, timeout=10, doc=""):
        my_logger.info("在页面{0}中是否存在元素{1}".format(doc, locator))

        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            my_logger.info("{0}秒内页面{1}中存在元素{2}".format(timeout, doc, locator))
            return True
        except:
            my_logger.error("{0}秒内页面{1}中不存在元素{2}".format(timeout, doc, locator))
            return False

    # 上下左右滑动
    # 从下向上滑
    def swipe_up(self, size):
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1, 300)
        pass

        # 从上向下滑

    def swipe_down(self, size):
        self.driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9, 300)
        pass

        # 从右向左滑

    def swipe_left(self, size):
        self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 300)
        pass

        # 从左向右滑

    def swipe_right(self, size):
        self.driver.swipe(size["width"] * 0.1, size["height"] * 0.5, size["width"] * 0.9, size["height"] * 0.5, 300)
        pass

    # 获取屏幕大小
    def get_size(self):
        return self.driver.get_window_size()

    # toast获取

    def get_toastMsg(self, str):
        # loc = (MobileBy.XPATH, '//*[contains(@text,"{}")]'.format("教室号不能为空"))
        loc = '//*[@text="{}"]'.format(str)
        # 等待时  要用元素存在条件
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located((AppiumBy.XPATH, loc)))
            return self.driver.find_element_by_xpath(loc).text
        except:
            my_logger.info("没有找到toast!!!!")
            raise

    # h5切换

    # alert处理
    def alert_action(self, action="accept"):
        pass

    # iframe切换
    def switch_iframe(self, iframe_reference):
        pass

    def upload_file(self):
        pass

    def save_screenshot(self, doc):
        # 图片名称:模块名_页面名称操作名称_年-月-日_ 时分秒. png
        # 当前时间
        file_name = dir_config.test_Screenshot_path + \
                    "{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(file_name)
            my_logger.info("截取网页成功。文件路径为: {0}".format(file_name))
        except:
            my_logger.error("截图失败")

    # 重写定义send_keys方法
    def sendKeys(self, value, locator, doc, clear=True):
        try:
            ele = self.get_element(locator, doc)
            if clear:
                ele.clear()
            ele.send_keys(Keys.CONTROL, 'a')
            ele.send_keys(value)
            my_logger.info("输入内容:{0}，在控件元素信息：{1}".format(value, locator))
        except:
            logging.error("输入内容操作失败，控件元素信息：{}".format(locator))
            print("输入内容操作失败，控件元素信息：{}".format(locator))
            # raise Exception("输入内容操作失败")
            # logging.error("错误信息为:{0}".format(traceback.format_exc()))
            assert False, "输入内容操作失败"


if __name__ == '__main__':
    # from selenium import webdriver
    # from PageObjects.login_page import LoginPage
    # from PageLocators.loginpage_locators import LoginPageLocators as loc
    # from selenium.webdriver.common.by import By
    #
    # sss = webdriver.Chrome()
    # sss.get("http://139.217.86.180:6092/#/login")
    # lg = LoginPage(sss)
    # doc = "登录页面——登录功能"
    # lg.wait_eleVisible(loc.name_text,doc = doc)
    # lg.input_text()
    #
    # sss.quit()

    pass
