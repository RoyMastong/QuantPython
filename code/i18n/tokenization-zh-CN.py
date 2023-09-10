# -*- coding = utf-8 -*-

# @time:2023/9/11 05:59
# @Author:Junqi Chen
# @File:tokenization-zh-CN.py
# @Software:PyCharm
import jieba
import jieba.posseg as pseg

if __name__ == "__main__":
    # 加载自定义词典
    jieba.load_userdict('my_dict.txt')

    text = "蔚来汽车是一家汽车公司，主营车型有ET5和ES8。"

    # 使用jieba进行分词和词性标注
    words = pseg.cut(text)

    # 遍历词汇和它们的词性标签
    for word, flag in words:
        print(f"词汇：{word}，词性：{flag}")

