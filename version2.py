# -*- coding: utf-8 -*-  
import requests
import json
import time
import re


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'zh-CN',
    'Connection': 'keep-alive',
    'Content-Length': '16',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'm.instrument.com.cn',
    'Origin': 'https://m.instrument.com.cn',
    'Referer': 'https://m.instrument.com.cn/show/activity/CZDetail2018/925?from=timeline&isappinstalled',
    'User-Agent': 'Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.3029.110 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = "https://m.instrument.com.cn/show/activity/czaddvote/925"
r = requests.post(url=url, headers=headers)

#def WriteIPadress():
#    all_url = []  # 存储IP地址的容器
    # 代理IP的网址
#    url = "http://api.xicidaili.com/free2017.txt"
#    r = requests.get(url=url)
#    all_url = re.findall("\d+\.\d+\.\d+\.\d+\:\d+", r.text)
#    with open("D:\\code\\python\\new\\Brush ticket\\IP.txt", 'w') as f:
#        for i in all_url:
#            f.write(i)
 #           f.write('\n')
 #   return all_url

#while count < 4000:
#    all_url = WriteIPadress()
#    for i in all_url:
#        try:
#            r = requests.post(url=url,headers=headers, timeout=10)
#            if(r.json()['flag'] == True):
#                count += 1
#                print("成功投票%d次！" % (count))
#            print(r.json())
#        except Exception as reason:
#            print("错误原因是：", reason)
