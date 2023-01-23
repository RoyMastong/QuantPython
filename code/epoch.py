# -*- coding = utf-8 -*-

# @time:2023/1/24 00:44
# @Author:Junqi Chen
# @File:epoch.py
# @Software:PyCharm

# 随机基线算法
import numpy as np

ssp = [1, 1, 1, 1, 0]
asp = [1, 0]


def main():
    epoch()
    rl = np.array([epoch() for _ in range(15)])
    print(rl)


def epoch():
    tr = 0
    for _ in range(100):
        a = np.random.choice(asp)
        s = np.random.choice(ssp)
        if a == s:
            tr += 1
    return tr


#冒泡算法示例







# 主函数
if __name__ == '__main__':
    main()
