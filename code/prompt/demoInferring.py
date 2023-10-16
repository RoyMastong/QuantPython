# -*- coding = utf-8 -*-

# @time:2023/10/12 17:35
# @Author:Junqi Chen
# @File:demoInferring.py
# @Software:PyCharm
import time

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


lamp_review = """ 
    Needed a nice lamp for my bedroom, and this one had \
     additional storage and not too high of a price point. \
      Got it fast. The string to our lamp broke during the \
       transit and the company happily sent over a new one. \
        Came within a few days as well. It was easy to put \
    together. I had a missing part, so I contacted their \
     support and they very quickly got me the missing piece! \
      Lumina seems to me to be a great company that cares \
       about their customers and products!!
       """


story = """
9月15日，蔚来智能电动轿跑SUV——全新EC6正式上市，车型起售价358,000元（75kWh电池包）。即日起，用户即可前往蔚来展厅试驾体验，新车交付也同步开启。

第一代蔚来EC6于2020年7月正式上市，成功开创了高端中型纯电轿跑SUV的细分市场，在不到3年的时间里，累计交付超过5万台，成为该细分市场的王者车型。
诞生于NT2.0平台的全新EC6实现了全面进化，以创新的家族设计、极致的性能和领先的智能，为热衷探索生活灵感，追求格调的家庭和个人用户带来超越期待的出行体验。

全新EC6车身长4849mm，宽1995mm，高1697mm，轴距为2915mm。新车采用轿跑溜背造型，勾勒出更具张力的车身曲线，经过反复优化的A柱倾角与更低的车身
高度带来流畅且舒展的车顶流线，配合双模主动升降尾翼，风阻低至0.24Cd。尾部饱满的曲面和隆起的宽肩融合，与收窄的后风挡形成强烈的反差感。
23°运动反切角设计降低了尾部的视觉厚度，让车尾更显动感。

在"Design for AD"的家族设计语言基础上，全新EC6再次创新，首次采用分体结构Double Dash日间行车灯。分体设计强化车头曲面张力，产生强烈的动势。
3D立体外露式设计与30mm超宽厚壁晶体，带来极致通透的视觉感受。同时新车通过工艺创新，消除了车灯上沿的黑色边框，引领新的设计潮流。

全新EC6搭载双模主动升降尾翼，长度为1,353mm，宽度为196mm，迎风受力面积为0.254㎡，风阻优化最高达10%。
尾翼采用减阻和极速两段式开启设计，并提供自动和手动两种模式。当车速高于80km/h时，尾翼将开启至减阻挡，开启角度为23°，风阻降至最低的0.24Cd；
当车速上升到170km/h，尾翼开启至极速挡，开启角度达到31.5°，在200km/h极速工况下，最大可额外提供580N的整车下压力，增强操控信心和整车稳定性。

全新EC6提供9种外观色，专属外观色“灵境紫”的灵感来自人工智能增强现实中的虚拟天空。
新车座舱延续蔚来「第二起居室」理念，环抱式设计打造有温度的内饰氛围。新车提供4种内饰主题色可选，其中，丹霞红、晨湖蓝、薄藤紫为专属内饰主题色。
在内饰细节方面，隐藏式智能出风口、同色柔光饰条、精致微动按键，融合可再生藤木材料以及门板下方声学织物材料，营造出更简洁、更精致、更富层次感的车内氛围。
全车59处隔音优化，为全新EC6带来了高水准的NVH表现。

全新EC6的全景天幕整体面积为1.770㎡，采光面积为1.156㎡，采用4.96mm双层隔音隔热玻璃，可选装EC光感天幕玻璃。应用第三代柔性电致变色技术，
EC光感天幕玻璃在亮态时透光率为6%，总能量隔绝率85%；暗态时透光率为1%，总能量隔绝率86.3%，紫外线隔绝率高达99.9%。

源于蔚来自研高端座椅平台，全新EC6的一体式运动座椅设计能够充分贴合人体脊柱生理曲线，兼顾激烈驾驶的包裹性与家用出行的舒适性，配合S-Shape原生座舱布局，
带来更加舒展、宽敞的空间感受。主驾座椅支持16向电动调节，副驾座椅支持18向电动调节，后排座椅靠背角度支持前后8°电动调节。
第二代女王副驾可实现最大172°的靠背倾角，并提供一键舒享和一键舒躺模式，带来真正双120°零重力体验。前排座椅具备加热、通风与8点式指压按摩功能，
通风采用体感更好的吸风模式，8点式指压按摩力度到位，模式丰富。新车方向盘也具备加热功能。全方位的舒适功能，让驾乘者时刻都能感受到愉悦与惬意。
通过充分挖掘空间潜能，全新EC6拥有出色的车内空间，获得了更高的「得房率」。全车共计22处储物空间，提供7处挂钩，总计可悬挂30kg重物。
后备箱容积594L，并提供多层隐藏储物空间，容积89L。第二排座椅支持4/2/4放倒，座椅靠背整体放倒后，后备箱最大容积扩展至1,402L。

高性能始终都是蔚来的基因。全新EC6标配双电机智能四驱系统，前150kW感应电机和后210kW永磁电机相结合，总功率达到360kW，扭矩达到700N·m，
半载工况下百公里加速仅4.4s。新车前轮标配蔚来自研高性能铝合金四活塞定钳和直径355mm的大尺寸刹车盘，百公里制动距离最短为34.5米（21英寸轮圈）。

全新EC6车身采用铝合金及高强度钢铝混合架构，兼顾性能与重量。采用一体式压铸工艺打造的全铝车身后地板和C/D柱，具有优异的安全性能，
充分保护电池和乘员安全，同时大量减少零部件数量，降低材料重量。接近50:50的车身前后轴荷比与580mm超低整车重心，有利于获得更好的中性转向特性，
提高过弯时的操控性能和速度极限。
"""

topic_list = ["EC6", "蔚来", "欧洲", "员工满意度", "ET5T"]

def textMotion():
    prompt = f""" 
    What is the sentiment of the following product review, which is delimited with triple backticks?

    Review text: '''{lamp_review}''' 
    """
    response = get_completion(prompt)
    print(response)


def textSingleMotion():
    prompt = f""" 
        What is the sentiment of the following product review, which is delimited with triple backticks?
        Give your answer as a single word, either "positive" \
        or "negative".
        Review text: '''{lamp_review}''' 
        """
    response = get_completion(prompt)
    print(response)


def textFiveMotion():
    prompt = f""" 
       Identify a list of emotions that the writer of the \
        following review is expressing. Include no more than \
        five items in the list. Format your answer as a list of \
        lower-case words separated by commas.
        Review text: '''{lamp_review}''' 
        """
    response = get_completion(prompt)
    print(response)


def textAngerMotion():
    prompt = f""" 
           Is the writer of the following review expressing anger?\
            The review is delimited with triple backticks. \
             Give your answer as either yes or no.
            Review text: '''{lamp_review}''' 
            """
    response = get_completion(prompt)
    print(response)


def textItemAndBrand():
    prompt = f""" 
        Identify the following items from the review text:

        - Item purchased by reviewer

        - Company that made the item

        The review is delimited with triple backticks. \
         Format your response as a JSON object with \
          "Item" and "Brand" as the keys.

        If the information isn't present, use "unknown" \
         as the value.

        Make your response as short as possible.
        Review text: '''{lamp_review}''' 
    """
    response = get_completion(prompt)
    print(response)


def textIntegrated():
    prompt = f""" 
        Identify the following items from the review text:

        - Sentiment (positive or negative)

        - Is the reviewer expressing anger? (true or false)

        - Item purchased by reviewer

        - Company that made the item

        The review is delimited with triple backticks. \
         Format your response as a JSON object with \
          "Sentiment", "Anger", "Item" and "Brand" as the keys. If the information isn't present, use "unknown" \
           as the value.

        Make your response as short as possible.

        Format the Anger value as a boolean.
            Review text: '''{lamp_review}''' 
        """
    response = get_completion(prompt)
    print(response)


def textTopicInfer():
    prompt = f"""
     Determine five topics that are being discussed in the \
      following text, which is delimited by triple backticks.

    Make each item one or two words long.
    
    Format your response as a list of items separated by commas.

    Text sample: '''{story}''' 
    """
    response = get_completion(prompt)
    response.split(sep=',')
    print(response)


def textTopicIndex():
    prompt = f""" 
    Determine whether each item in the following list of \
     topics is a topic in the text below, which is delimited with triple backticks.

    Give your answer as list with 0 or 1 for each topic. \
    And format is like this: [topic:0, topic:1, topic:0, topic:1, topic:0]
    List of topics: {", ".join(topic_list)}
    Text sample: '''{story}'''
    
    """
    response = get_completion(prompt)
    print(response)
    response = response.strip('[]')  # 去除字符串中的方括号
    topic_dict = {i.split(':')[0]: int(i.split(':')[1]) for i in response.split(sep=', ')}
    if topic_dict['EC6'] == 1:
        print("ALERT: New EC6 story!")


if __name__ == '__main__':
    _ = load_dotenv(find_dotenv())
    # 时间开始
    start_time = time.time()
    openai.api_key = CHATGPT_CONFIG.get('api.key')

    # textMotion()
    # textSingleMotion()
    # textFiveMotion()
    # textAngerMotion()
    # textItemAndBrand()
    # textIntegrated()
    # textTopicInfer()
    textTopicIndex()

    # 时间结束
    end_time = time.time()
    print("程序运行时间：", end_time - start_time)
