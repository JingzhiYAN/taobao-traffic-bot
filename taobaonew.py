#coding:utf-8
import re
import time
from random import choice
import requests
from urllib import request
from bs4 import BeautifulSoup
import multiprocessing
import time
import urllib


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

urlt = "https://s.taobao.com/search?q=%E6%95%8F%E6%84%9F%E8%82%8C%E8%82%A4cellapy&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20181225&ie=utf8";
#執行pro

ipis = get_ip();
tt = 0
for a3 in ipis:
    proxy_handler = urllib.request.ProxyHandler({'http': a3});
    opener = urllib.request.build_opener(proxy_handler);
    urllib.request.install_opener(opener);
    print (ipis);
    usera = selectUserAgent();
    req = urllib.request.Request(url=urlt, headers=usera,);
    urllib.request.urlopen(req)
    html = req.read();
    if "egf寡肽" in html:
        print("搞定一个");
    else:
        print("砸了一个");
    if '未连接到互联网' in driver.page_source:
        print('代理不好使啦')
        continue
    if 'anti_Spider-checklogin&' in driver.page_source:
        print('被anti_Spider check啦')
        break
    if '无法访问此网站' in driver.page_source:
        print('代理太慢啦！')
        continue

    time.sleep(1)
    print(success)
    tt = tt+1;