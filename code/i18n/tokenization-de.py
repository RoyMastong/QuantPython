# -*- coding = utf-8 -*-

# @time:2023/9/11 06:15
# @Author:Junqi Chen
# @File:tokenization-de.py
# @Software:PyCharm
import spacy


if __name__ == "__main__":
    # 加载德文语言模型
    nlp = spacy.load("de_core_news_sm")

    text = "Das Wetter in Berlin ist heute schön."

    # 处理文本
    doc = nlp(text)

    # 遍历分词和词性标注结果
    for token in doc:
        print(f"词汇：{token.text}，词性：{token.pos_}")

