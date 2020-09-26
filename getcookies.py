# coding:utf-8
import time
import json
import requests
import urllib3
from urllib.request import urlretrieve

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 读取设置的账号密码
import account
import getNum

driver = webdriver.Chrome()
https = urllib3.PoolManager()

driver.get('https://www.okcis.cn/search/')  # 打开网页
ele=driver.find_element_by_xpath("//a[@class='denglu_lia_20141021']")
ActionChains(driver).move_to_element(ele).perform()

# 定位iframe，暂时没有实现自动翻页
iframe_name = "site-top-login-iframe"
iframe = driver.find_element_by_name(iframe_name)
iframe_location = iframe.location
driver.switch_to.frame(iframe)

driver.find_element_by_xpath("//input[@name='username']").send_keys(account.account_phone)
driver.find_element_by_xpath("//input[@name='password']").send_keys(account.account_password)

try:
    print('请在10秒内输入验证码')
    time.sleep(10)
    # img = driver.find_element_by_xpath("//li[@class='inde_dlli_20141021']/img[@class='yztupian_im_20141021']")

    # num = getNum.getCodeImg(driver, img, iframe_location['x'] + 560, iframe_location['y'])
    # print(num)
    # # headers = {
    # #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    # # }

    # # res = https.request('GET', url, headers=headers, preload_content=False)
    # # num = getNum.getNum(res.data)
    # # print(num)
    # num = eval(num)
    # print(num)

    # driver.find_element_by_xpath("//input[@name='yzm']").send_keys(num)
    driver.find_element_by_xpath("//input[@name='iframe-login-submit']").click()

except:
    print('error!please try again')
    driver.quit()

else:
    cookies = driver.get_cookies()
    jsoncookies = json.dumps(cookies)
    with open('cookies.txt', 'w') as f:
        f.write(jsoncookies)
    print('Get Cookies successfully')

    driver.quit()
