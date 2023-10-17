
# -*- coding = utf-8 -*-

# @time:2023/10/16 15:45
# @Author:Junqi Chen
# @File:demoForTransforming.py
# @Software:PyCharm
import time

import openai
import os

from dotenv import load_dotenv, find_dotenv

from code.prompt.config import CHATGPT_CONFIG
from IPython.display import display, Markdown, Latex, HTML, JSON


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


user_messages = [ "La performance du système est plus lente que d'habitude.", # System performance is slower than normal

"Mi monitor tiene píxeles que no se iluminan.", # My monitor has pixels that are not lighting

"Il mio mouse non funziona", # My mouse is not working

"Mój klawisz Ctrl jest zepsuty", # My keyboard has a broken control key

"我的屏幕在闪烁" # My screen is flashing
]

data_json = { "resturant employees" :
                  [ {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
                    {"name":"Bob", "email":"bob32@gmail.com"},
                    {"name":"Jai", "email":"jai87@gmail.com"}
                    ]
            }

text = [ "The girl with the black and white puppies have a ball.", # The girl has a ball.
"Yolanda has her notebook.", # ok
"Its going to be a long day. Does the car need it’s oil changed?", # Homonyms
"Their goes my freedom. There going to bring they’re suitcases.", # Homonyms
"Your going to need you’re notebook.", # Homonyms
"That medicine effects my ability to sleep. Have you heard of the butt erfly affect?", # Homonyms
"This phrase is to cherck chatGPT for speling abilitty" # spelling
]


def textTranslate():
    prompt = f"""
    Translate the following text to French and Spanish and Chinese: 
     ```I want to order a basketball```
    """
    response = get_completion(prompt)
    print(response)


def generalTranslator():
    for issue in user_messages:
        prompt = f"Tell me what language this is: ```{issue}```"
        lang = get_completion(prompt)
        print(f"Original message({lang}): {issue}")

        prompt = f"""
        Translate the following text to English and Korean:\
        ```{issue}```
        """
        response = get_completion(prompt)
        print(response, "\n")


def textTone():
    prompt = f"""
    将以下内容从俚语翻译成商业信函:
    '老哥，我是俊琦，帮我看看这盏落地灯的规格呗。'
    """
    response = get_completion(prompt)
    print(response)


def textFormatTrans():
    prompt = f"""
    Translate the following python dictionary from JSON to an HTML \
     table with column headers and title: {data_json}
    """
    response = get_completion(prompt)
    print(response)
    display(HTML(response))


def textProofread():
    for t in text:
        prompt = f"""
        Proofread and correct the following text and rewrite the corrected version.
        If you don't find and errors, just say "No errors found". Don't use any punctuation around the text:
         ```{t}```"""
        response = get_completion(prompt)
        time.sleep(60)
        print(response)


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv())
    # 时间开始
    start_time = time.time()
    openai.api_key = CHATGPT_CONFIG.get('api.key')

    # textTranslate()
    # generalTranslator()
    # textTone()
    # textFormatTrans()
    textProofread()


    # 时间结束
    end_time = time.time()
    print("程序运行时间：", end_time - start_time)
