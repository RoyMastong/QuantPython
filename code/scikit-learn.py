# -*- coding = utf-8 -*-

# @time:2023/1/24 21:40
# @Author:Junqi Chen
# @File:scikit-learn.py
# @Software:PyCharm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPRegressor


def main():
    x = np.linspace(-2, 4, 25)
    y = f(x)
    model = MLPRegressor(hidden_layer_sizes=3 * [256], learning_rate_init=0.03, max_iter=5000)
    model.fit(x.reshape(-1, 1), y)
    y_ = model.predict(x.reshape(-1, 1))
    MSE = ((y - y_) ** 2).mean()
    print(MSE)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'ro', label='sample data')
    plt.plot(x, y_, lw=3.0, label='dnn estimation')
    plt.legend()
    plt.show()


def f(x):
    return 2 * x ** 2 - x ** 3 / 3


if __name__ == '__main__':
    main()
