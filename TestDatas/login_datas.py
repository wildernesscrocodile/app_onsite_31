#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :login_datas.py
# @Time      :2020/10/13 11:33
# @Author    :麻花

# 正常场景 - 测试数据
success_data = {"user": "14311233333", "passwd": "huiyi@31"}

# 异常场景 - 用户被锁定、不存在的用户名
phone_data = [
    {"user": "", "passwd": "123456", "check": "请输入账号 ！"},
    {"user": "", "passwd": "123456", "check": "请输入账号 ！"}

]

# 异常场景 - 用户被锁定、不存在的用户名
wrongPwd_noReg_data = [
    {"user": "0001352", "passwd": "123456", "check": "错误：未找到您的个人信息，请联系管理员！"},
    {"user": "6433623464", "passwd": "123456", "check": "错误：用户账户不存在"}
]
