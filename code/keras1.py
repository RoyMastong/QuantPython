# -*- coding = utf-8 -*-

# @time:2023/1/24 23:25
# @Author:Junqi Chen
# @File:keras1.py
# @Software:PyCharm
import numpy as np
import tensorflow as tf
from keras.layers import Dense
from keras.models import Sequential
import matplotlib.pyplot as plt


def main():
    tf.random.set_seed(100)
    model = Sequential()
    model.add(Dense(256, input_dim=1, activation='relu'))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    x = np.linspace(-2, 4, 25)
    y = f(x)
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ro', label='sample data')
    for _ in range(1, 6):
        model.fit(x, y, epochs=1000, verbose=False)
        y_ = model.predict(x)
        MSE = ((y - y_.flatten()) ** 2).mean()
        print(f'round {_}: MSE = {MSE:.5f}')
        plt.plot(x, y_, '--', label=f'round {_}')
        plt.legend()
        plt.show()


def f(x):
    return 2 * x ** 2 - x ** 3 / 3


def main1():
    np.random.seed(0)
    x = np.linspace(-1, 1)
    y = np.random.random(len(x)) * 2 - 1
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ro', label='sample data')
    for deg in [1, 5, 9, 11, 13, 15]:
        reg = np.polyfit(x, y, deg=deg)
        y_ = np.polyval(reg, x)
        MSE = ((y - y_) ** 2).mean()
        print(f'deg {deg:2d}: MSE = {MSE:.5f}')
        plt.plot(x, np.polyval(reg, x), label=f'deg= {deg}')
        plt.legend()
    plt.show()






if __name__ == '__main__':
    # main()
    main1()
