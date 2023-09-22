# -*- coding = utf-8 -*-

# @time:2023/9/21 02:47
# @Author:Junqi Chen
# @File:demoForIphone.py
# @Software:PyCharm

from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.select import Select
import time

print("hello world")

import time

# iphone12 自动化测试
print("iphone12 自动化测试开始")

# 访问测试的url定义
url = "https://www.apple.com.cn/shop/buy-iphone/iphone-15"

# 1. 创建浏览器对象  这里的Chrome中的变量是chromedriver的驱动地址
driver = webdriver.Chrome()

# 2. 跳转到apple官网
driver.get(url)

# 3. 隐式等待 设置 防止预售的网络的阻塞
driver.implicitly_wait(10)

# 4.1 开始选择规格【此处我选择了-12 mini】
# element_sku = driver.find_element_by_name('dimensionScreensize')
# driver.implicitly_wait(10)
# element_sku.click()


print("end")