#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: test_meetlist.py
# @Author: 麻花
# @Institution: --- University, ---, China
# @Site: 
# @Time:  2022 01 4月
# ---


from PageObjects.login_page import LoginPage
from TestDatas import login_datas as LD
from TestDatas import meet_list_datas as MD
from PageObjects.meet_list_page import MeetList_page
from Common.logger import MyLog
from PageLocators.meet_list_locators import MeetListLocator as loc
from Common.basepage import BasePage


import pytest


my_logger = MyLog()
# data = [{"noReset": "True"}]

@pytest.mark.usefixtures("start_app")
class TestMeetlist:

    #   搜索会议
    @pytest.mark.parametrize("start_app", [{"noReset": "True"}], indirect=True)
    def test_search_conference(self, start_app):
        LoginPage(start_app).login(LD.success_data["user"], LD.success_data["passwd"])
        MeetList_page(start_app).search_conference(MD.conference_data["conferenceName"])

        assert BasePage(start_app).is_eleExist(loc.search_page_conferencename)
        pytest.assume(1 + 4 == 5)
        pytest.assume(BasePage(start_app).is_eleExist(loc.search_page_conferencename))


if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra", "test_meetlist.py"])




