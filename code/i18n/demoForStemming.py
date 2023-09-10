# -*- coding = utf-8 -*-

# @time:2023/8/28 04:31
# @Author:Junqi Chen
# @File:demoForStemming.py
# @Software:PyCharm

from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer

word = 'fishing'


# 基于Porter词干提取算法
def Porter():
    porter_stemmer = PorterStemmer()
    a1 = porter_stemmer.stem(word)
    print("基于Porter词干提取算法：" + a1)


# 基于Lancaster 词干提取算法
def Lancaster():
    lancaster_stemmer = LancasterStemmer()
    a2 = lancaster_stemmer.stem(word)
    print("基于Lancaster 词干提取算法：" + a2)


# 基于Snowball 词干提取算法
def Snowball():
    snowball_stemmer = SnowballStemmer("english")
    a3 = snowball_stemmer.stem(word)
    print("基于Snowball 词干提取算法：" + a3)


if __name__ == '__main__':
    Porter()
    Lancaster()
    Snowball()
