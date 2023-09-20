# -*- coding = utf-8 -*-

# @time:2023/9/19 17:01
# @Author:Junqi Chen
# @File:demo1.py
# @Software:PyCharm


import openai
import os

from dotenv import load_dotenv, find_dotenv


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

    openai.api_key = os.getenv('OPENAI_API_KEY')
