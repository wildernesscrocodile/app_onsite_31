# @Time : 2021/4/6 13:46 

# @Author : 麻花

# @File : dir_config.py 

# @Software: PyCharm


import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)

# 测试数据路径
test_datas_path = os.path.join(project_path, 'TestDatas')

# 测试用例路径
test_cases_path = os.path.join(project_path, 'TestCases')

# 测试报告路径
test_html_report_path = os.path.join(project_path, 'Outputs', 'Report\\')

# 存储日志文件路径
test_log_path = os.path.join(project_path, 'Outputs', 'Logs\\')

# 测试截图路径
test_Screenshot_path = os.path.join(project_path, 'Outputs', 'Screenshots\\')

caps_dir = os.path.join(project_path, 'Desired_Caps')
