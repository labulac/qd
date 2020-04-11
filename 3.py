from datetime import time

from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('-headless')
option.add_argument('-no-sandbox')
option.add_argument('-incognito')
option.add_argument('-blink-settings=imagesEnabled=false')
option.add_argument('-ignore-certificate-errors')
option.add_argument('-start-maximized')
option.add_argument('-hide-scrollbars')
option.add_argument('–single-process')
option.add_argument('–lang=zh-CN')
option.add_argument('–disable-images')

driver = webdriver.Chrome(chrome_options=option)
driver.get('https://www.alexamaster.net/Master/141662')
time.sleep(600)
driver.quit()