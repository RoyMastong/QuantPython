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
    # epoch()
    epoch1()
    rl = np.array([epoch1() for _ in range(15)])
    print(rl)
    print(rl.mean())


def epoch():
    tr = 0
    for _ in range(100):
        a = np.random.choice(asp)
        s = np.random.choice(ssp)
        if a == s:
            tr += 1
    return tr


def epoch1():
    tr = 0
    asp1 = [0, 1]
    for _ in range(100):
        a = np.random.choice(asp1)
        s = np.random.choice(ssp)
        if a == s:
            tr += 1
        asp1.append(s)
    return tr


# 主函数
if __name__ == '__main__':
    main()
