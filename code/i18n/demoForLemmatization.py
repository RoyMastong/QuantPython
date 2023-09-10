# -*- coding = utf-8 -*-

# @time:2023/8/28 05:04
# @Author:Junqi Chen
# @File:demoForLemmatization.py
# @Software:PyCharm

# 引入lemminflect.getLemma
import lemminflect

from nltk.stem import WordNetLemmatizer
# 基于NLTK的词形还原实现
def by_nltk(word, pos):
    """ 使用nltk.stem.WordNetLemmatizer实现词性还原
    :param word: <str> 单词
    :param pos: <str> 词性
    :return: <str> 词性还原结果
    """
    lemmatizer = WordNetLemmatizer()
    return lemmatizer.lemmatize(word, pos.lower())

def by_lemminflect(word, pos):
    """ 使用lemminflect.getLemma实现词性还原
    :param word: <str> 单词
    :param pos: <str> 词性
    :return: <str> 词性还原结果
    """
    if pos.lower() == "a":
        pos = "ADJ"
    elif pos.lower() == "n":
        pos = "NOUN"
    elif pos.lower() == "v":
        pos = "VERB"
    elif pos.lower() == "p":
        pos = "PROPN"
    return lemminflect.getLemma(word, pos)



if __name__ == "__main__":
    test_word_list = [["men", "n"], ["computer", "n"], ["ate", "v"], ["running", "v"], ["saddest", "a"],
                      ["fancier", "a"]]
    for test_word in test_word_list:
        print(by_lemminflect(test_word[0], test_word[1]))


