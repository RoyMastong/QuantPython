
# -*- coding = utf-8 -*-

# @time:2023/9/11 15:49
# @Author:Junqi Chen
# @File:sorted.py
# @Software:PyCharm

if __name__ == "__main__":
    # 原始列表
    unsorted_list = ["apple", "banana", "cherry", "date", "fig"]

    # 自定义的排序函数：按照字符串的长度排序
    def custom_sort_key(item):
        return len(item)

    # 使用sorted()函数并指定自定义的排序规则
    sorted_list = sorted(unsorted_list, key=custom_sort_key)

    # 输出排序后的结果
    print("按照字符串长度排序结果:", sorted_list)
    print('hhhh')
