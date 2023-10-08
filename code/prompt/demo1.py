# -*- coding = utf-8 -*-

# @time:2023/9/19 17:01
# @Author:Junqi Chen
# @File:demo1.py
# @Software:PyCharm


import openai
import os

from dotenv import load_dotenv, find_dotenv

from code.prompt.config import CHATGPT_CONFIG


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def useDelimiters():
    text = f"""
       You should express what you want a model to do by \
        providing instructions that are as clear and \
         specific as you can possibly make them. \
          This will guide the model towards the desired output, \
           and reduce the chances of receiving irrelevant \
            or incorrect responses. Don't confuse writing a \
             clear prompt with writing a short prompt. \
              In many cases, longer prompts provide more clarity \
        and context for the model, which can lead to \
         more detailed and relevant outputs.
        """
    prompt = f"""Summarize the text delimited by triple backticks \
         into a single sentence.
         ```{text}```"""

    responce = get_completion(prompt)
    print(responce)

def askForStructuredOutput():
    prompt = f"""
    Generate a list of three made-up book titles along\
    with their authors and genres. Provide them in JSON format with the following keys:
    book_id, title, author, genre.
    """
    response = get_completion(prompt)
    print(response)


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv())

    openai.api_key = CHATGPT_CONFIG.get('api.key')
    # useDelimiters()
    askForStructuredOutput()



