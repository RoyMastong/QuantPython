# -*- coding = utf-8 -*-

# @time:2023/9/11 05:46
# @Author:Junqi Chen
# @File:tokenization.py
# @Software:PyCharm
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

if __name__ == "__main__":
    nltk.download('punkt')  # 下载必要的数据
    text = "The quick brown fox jumps over the lazy dog. Das Wetter ist heute schön."
    # 使用NLTK进行分词
    tokens = word_tokenize(text)
    # 使用NLTK进行词性标注
    tagged_tokens = pos_tag(tokens)
    # 分离形容词和名词
    adjectives = [token for token, pos in tagged_tokens if pos.startswith('JJ')]
    nouns = [token for token, pos in tagged_tokens if pos.startswith('NN')]
    print("形容词：", adjectives)
    print("名词：", nouns)








