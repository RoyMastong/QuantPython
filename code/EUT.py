# -*- coding = utf-8 -*-

# @time:2023/1/26 03:06
# @Author:Junqi Chen
# @File:EUT.py
# @Software:PyCharm


import numpy as np
from scipy.optimize import minimize


def u(x):
    return np.sqrt(x)


S0 = 10
B0 = 10

S1 = np.array((20, 5))
B1 = np.array((11, 11))

M0 = np.array((S0, B0))
M1 = np.array((S1, B1)).T

phi_A = np.array((0.75, 0.25))
phi_D = np.array((0.25, 0.75))

flag = np.dot(M0, phi_A) == np.dot(M0, phi_D)
A1 = np.dot(M1, phi_A)
D1 = np.dot(M1, phi_D)
P = np.array((0.5, 0.5))

w = 10
cons = {'type': 'eq', 'fun': lambda phi: np.dot(M0, phi) - w}


def EUT(x):
    return np.dot(P, u(x))


def EUT_(phi):
    x = np.dot(M1, phi)
    return EUT(x)


opt = minimize(lambda phi: -EUT_(phi), x0=phi_A, constraints=cons)

result = EUT_(opt['x'])


def main():
    print(flag)
    print(A1)
    print(D1)
    print(EUT(A1))
    print(EUT(D1))
    print(opt)
    print(result)
    print("hello world陈俊琦")


if __name__ == '__main__':
    main()
