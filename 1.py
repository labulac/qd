import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def push(name):
    url = "https://maker.ifttt.com/trigger/ppp/with/key/bm4a3i-fD-1FDWMKC4pqc1"
    payload = "{\n    \"value1\": \"" + name + "\"\n}"
    headers = {
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.15.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "a9477d0f-08ee-4960-b6f8-9fd85dc0d5cc,d376ec80-54e1-450a-8215-952ea91b01dd",
        'Host': "maker.ifttt.com",
        'accept-encoding': "gzip, deflate",
        'content-length': "63",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)

    print(response.text)


option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--headless')
option.add_argument('--incognito')
option.add_argument('--blink-settings=imagesEnabled=false')
option.add_argument('--start-maximized')
option.add_argument('--hide-scrollbars')


def macdo(u, p, url):
    try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='go-signin']")))

        driver.find_element_by_xpath("//*[@id='go-signin']").click()
        driver.find_element_by_xpath("//*[@id='user_login-input']").send_keys(u)
        driver.find_element_by_xpath("//*[@id='password-input']").send_keys(p)
        driver.find_element_by_xpath("//*[@class='btn btn-info btn-block submit']").click()
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='btn btn-warning btn-sm sign-btn']")))
        driver.find_element_by_xpath("//*[@class='btn btn-warning btn-sm sign-btn']").click()
    except Exception as error:
        print(error)
        push('用户名：' + u + '，地址：' + url + '，')


def pcbeta(u, p, url):
    try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input")))

        driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input").send_keys(u)

        driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/form/div/div[2]/table/tbody/tr/td[1]/input").send_keys(p)
        driver.find_element_by_xpath("//*[@class='pn pnc']").click()
        time.sleep(30)
        driver.get('http://i.pcbeta.com/home.php?mod=task&do=apply&id=149')
        time.sleep(30)
    except Exception as error:
        print(error)
        push('用户名：' + u + '，地址：' + url + '，')


macdo('740162752@qq.com', '1357954163', 'https://www.macdo.cn/')
macdo('18051735535@163.com', '1357954163', 'https://www.macdo.cn/')
pcbeta('labulac', 'Aa1357954163', 'http://bbs.pcbeta.com/member.php?mod=logging&action=login')
