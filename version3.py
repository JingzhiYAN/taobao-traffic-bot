#coding:utf-8
import re
import time
from random import choice

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


#隨機獲取一個header
def selectUserAgent():
    uas = [
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
        "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
        "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
        "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
        "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",
    ]
    return choice(uas)
#獲取代理IP
def get_ip():

    url = "http://www.xicidaili.com/nn"
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
                "Referer":"http://www.xicidaili.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
                }
    r = requests.get(url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    data = soup.table.find_all("td")
    ip_compile= re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>')    # 匹配IP
    port_compile = re.compile(r'<td>(\d+)</td>')                # 匹配端口
    ip = re.findall(ip_compile,str(data))                       # 获取所有IP
    port = re.findall(port_compile,str(data))                   # 获取所有端口
    return [":".join(i) for i in zip(ip,port)]                  # 组合IP+端口，如：115.112.88.23:8080

#執行pro

success=0
for num, ipport in enumerate(ips):
    result=str(num)+". 代理:"+ipport
    options =  webdriver.ChromeOptions();
    options.add_argument('lang=zh_CN.UTF-8');
    options.add_argument('--headless');
    options.add_argument('--no-sandbox');
    options.add_argument('user-agent="'+selectUserAgent()+'"');
    options.add_argument('--proxy-server=http://'+ipport);
    driver = webdriver.Chrome(chrome_options = options);
    driver.get('https://m.instrument.com.cn/show/activity/CZDetail2018/925?from=timeline&isappinstalled');
    driver.find_element_by_xpath("/html/body/div[@class='container']/article[@class='wrap-act']/section[@class='act-join']/div[@class='p10']/span[@class='cz_share_vote']").click();
    success+=1
    time.sleep(1)
    browser.quit()
    print("{0}成功,共成功{1}次".format(result,success))
