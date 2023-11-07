# -*- coding = utf-8 -*-

# @time:2023/11/7 15:58
# @Author:Junqi Chen
# @File:stat_time.py
# @Software:PyCharm
# @desc: statistics the execution time of a function
from datetime import datetime


def calculate_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        execution_time = end_time - start_time
        print(f'{func.__name__} 执行时间: {execution_time}')
        return result

    return wrapper