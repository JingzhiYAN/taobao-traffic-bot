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

    url = "https://www.xicidaili.com/nt"
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
ipis = get_ip();
success=0
for isi in ipis:
    options =  webdriver.ChromeOptions();
    options.add_argument('lang=zh_CN.UTF-8');
    #options.add_argument('--headless');
    options.add_argument('--no-sandbox');
    options.add_argument('user-agent="'+selectUserAgent()+'"');
    print('--proxy-server=http://'+isi);
    #options.add_argument('--proxy-server=https://%s' % isi);

    driver = webdriver.Chrome(chrome_options = options);
    driver.get('https://www.taobao.com');
    driver.get('https://s.taobao.com/search?q=cellapy%E4%BF%AE%E6%8A%A4%E9%9C%9C&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306');
    driver.get('https://detail.m.tmall.hk/item.htm?spm=a230r.1.14.4.6d8841celXL7CE&id=577128927497&cm_id=140105335569ed55e27b&abbucket=9')

    if '未连接到互联网' in driver.page_source:
        print('代理不好使啦')
        continue
    if 'anti_Spider-checklogin&' in driver.page_source:
        print('被anti_Spider check啦')
        break
    if '无法访问此网站' in driver.page_source:
        print('代理太慢啦！')
        continue

    driver.find_element_by_xpath("/html/body/div[@class='page']/section[@class='actionBar-bg']/div[@id='s-actionBar-container']/div[@class='action-bar-wrap j-bottom-bar  ']/div[@class='trade']/a[@class='cart ']").click();
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[@class='widgets-cover show']/div[@class='cover-content']/div[@class='sku-wrap']/div[@class='body']/div[@class='body-item']/ul[@class='sku-list-wrap']/li/div[@class='items']/a[2]").click();
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[@class='widgets-cover show']/div[@class='cover-content']/div[@class='sku-wrap']/div[@class='footer trade']/a[@class='ok']").click();
    time.sleep(1)
    driver.get('https://register.tmall.com/?spm=a2107.1.0.0.7dd28L508L50TS&f=login')

    time.sleep(1)
    print(success)
    print(isi)
    success+=1