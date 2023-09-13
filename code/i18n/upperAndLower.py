# -*- coding = utf-8 -*-

# @time:2023/9/11 15:26
# @Author:Junqi Chen
# @File:upperAndLower.py
# @Software:PyCharm


if __name__ == "__main__":
    texts = [
        "ıstanbul İzmir Türkiye",  # 土耳其语
        "Fußgängerüberweg",         # 德语
        "Hello, World!"            # 英语
    ]
    for text in texts:
        # 将文本从小写转换为大写
        uppercase_text = text.upper()
        # 将文本从大写转换为小写
        lowercase_text = text.lower()
        print(f"原文本: {text}")
        print(f"大写文本: {uppercase_text}")
        print(f"小写文本: {lowercase_text}")
        print("--------------------")

