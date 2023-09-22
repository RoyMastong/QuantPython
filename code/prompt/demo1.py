# -*- coding = utf-8 -*-

# @time:2023/9/19 17:01
# @Author:Junqi Chen
# @File:demo1.py
# @Software:PyCharm


import openai
import os

from dotenv import load_dotenv, find_dotenv
openai.api_key = "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"


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv())

    openai.api_key = "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"

    text = f"""
    蔚来汽车是一家2014年11月成立的全球化智能电动汽车公司，主要在中国境内销售高端智能电动汽车。\
    蔚来旗下的主要产品包括蔚来ES6、蔚来ES8、蔚来EC6等。\
    2018年9月，蔚来在纽约证券交易所上市，股票代码为NIO。
    """
    prompt = f"""将由三个反引号分隔的文本总结为一个句子。
     ```{text}```"""

    responce = get_completion(prompt)
    print(responce)

