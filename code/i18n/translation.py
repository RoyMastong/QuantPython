# -*- coding = utf-8 -*-

# @time:2023/9/10 20:14
# @Author:Junqi Chen
# @File:translation.py
# @Software:PyCharm
import translator as translator
from googletrans import Translator


def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language, src='auto')
    return translated_text.text


if __name__ == "__main__":
    # input_text = input("请输入要翻译的文本：")
    input_text = ("大家好，今天天气真不错！")
    target_language = input("请输入目标语言代码（例如：en 英语，zh-cn 中文等）：")

    translated_text = translate_text(input_text, target_language)
    print("翻译结果：", translated_text)
