# @Time : 2021/4/6 20:16 

# @Author : 麻花

# @File : test_login.py 

# @Software: PyCharm

from PageObjects.login_page import LoginPage
from TestDatas import login_datas as LD
from PageObjects.meet_list_page import MeetList_page

import pytest
from Common.logger import MyLog
from Common.commons import env


my_logger = MyLog()

@pytest.mark.usefixtures("start_app")
class TestLogin:

    #   正常用例一登陆成功
    @pytest.mark.smoke
    @pytest.mark.parametrize("start_app", [{"noReset": "False"}], indirect=True)
    def test_login_success(self, start_app):
        LoginPage(start_app).login(LD.success_data[env]["user"], LD.success_data[env]["passwd"])
        assert MeetList_page(start_app).get_loginStats()


if __name__ == '__main__':
    pytest.main(["-q", "--reruns 5", "-s", "-ra", "test_login.py"])

