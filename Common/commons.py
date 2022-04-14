#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: commons.py
# @Author: 麻花
# @Institution: --- University, ---, China
# @Site: 
# @Time:  2022 11 4月
# ---
import yaml

from Common.dir_config import caps_dir
from Common.get_properties import Properties

runenv = Properties("./Outputs/allure/environment.properties").getProperties()
env = runenv["environment"]

def get_appPackage():
    # 获取当前环境app包名
    fs = open(caps_dir + "/caps.yaml")
    caps = yaml.safe_load(fs)

    desired_caps = caps[env]

    return desired_caps["appPackage"]






