# -*- coding = utf-8 -*-

# @time:2023/1/25 21:48
# @Author:Junqi Chen
# @File:arbitragePricingTheory.py
# @Software:PyCharm

import numpy as np


def main():
    S0 = 10
    B0 = 10

    S1 = np.array((20, 5))
    B1 = np.array((11, 11))

    M0 = np.array((S0, B0))
    M1 = np.array((S1, B1)).T

    K = 14.5

    C1 = np.maximum(S1 - K, 0)
    phi = np.linalg.solve(M1, C1)
    flag = np.allclose(C1, np.dot(M1, phi))
    C0 = np.dot(M0, phi)
    print(C0, flag)


if __name__ == '__main__':
    main()
