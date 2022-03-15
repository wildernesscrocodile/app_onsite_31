# @Time : 2021/4/6 14:08 

# @Author : 麻花

# @File : generation_path.py

# @Software: PyCharm

import time
import os.path


class Generation_Path:

    def generate_path(self, path, format):
        current_time = time.strftime('%Y%m%d%H%M',
                                     time.localtime(time.time()))
        dir_time = time.strftime('%Y%m%d', time.localtime(time.time()))  # 返回当前时间的年月日作为目录名称
        isExists = os.path.exists(path + dir_time)
        if not isExists:
            os.makedirs(path + dir_time)
            # print(path + dir_time + "目录创建成功")
        # else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path + "目录 %s 已存在" % dir_time)
        path_name = path + dir_time + '\\' + current_time + format
        return path_name


if __name__ == '__main__':
    pass
