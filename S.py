#coding:utf-8
from selenium import webdriver
import time

i = 0
while(i<10000):
	option=webdriver.ChromeOptions();
	option.add_argument('--headless');
	option.add_argument('--no-sandbox');
	option.add_argument('--start-maximized');
	#driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application/chromedriver.exe' chrome_options=option)
	driver = webdriver.Chrome(chrome_options = option)
	#driver = webdriver.Chrome();
	driver.get('https://m.instrument.com.cn/show/activity/CZDetail2018/925?from=timeline&isappinstalled');
	#driver.maximize_window()
	time.sleep(1);
	driver.find_element_by_xpath("/html/body/div[@class='container']/article[@class='wrap-act']/section[@class='act-join']/div[@class='p10']/span[@class='cz_share_vote']").click();
	i = i+1;