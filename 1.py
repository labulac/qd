import time
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def update():
    with open('2.py', 'r') as f:
        a = f.read()

    r = requests.get("https://qd.labulac.top/2.py")
    b = r.text

    if a != b:
        print("检测到更新")
        with open("2.py", 'w') as f:
            f.write(b)
        print("更新脚本已更新完成")

    else:
        print("更新脚本没有更新")


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


update()
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


def qqlogin(u,p):
    driver = webdriver.Chrome(chrome_options=option)
    WebDriverWait(driver, 60).until(EC.presence_of_element_located(
        (By.XPATH, ".//*[@id='ptlogin_iframe']")))
    iframe = driver.find_element_by_xpath(".//*[@id='ptlogin_iframe']")
    driver.switch_to_frame(iframe)
    driver.find_element_by_xpath(".//*[@id='switcher_plogin']").click()
    driver.find_element_by_xpath(".//*[@id='u']").send_keys(u)
    driver.find_element_by_xpath(".//*[@id='p']").send_keys(p)
    driver.find_element_by_xpath(".//*[@id='login_button']").click()


def macdo(u, p, url,n):
    try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//*[@id='go-signin']")))

        driver.find_element_by_xpath("//*[@id='go-signin']").click()
        driver.find_element_by_xpath("//*[@id='user_login-input']").send_keys(u)
        driver.find_element_by_xpath("//*[@id='password-input']").send_keys(p)
        driver.find_element_by_xpath("//*[@class='btn btn-info btn-block submit']").click()
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//*[@class='btn btn-warning btn-sm sign-btn']")))
        driver.find_element_by_xpath("//*[@class='btn btn-warning btn-sm sign-btn']").click()
        time.sleep(5)
        driver.quit()
        print("ok")
    except Exception as error:
        print(error)
        push('用户名：' + u + '，站点：' + n + '，')


def pcbeta(u, p, url,n):
    try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input")))

        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input").send_keys(u)

        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div[2]/table/tbody/tr/td[1]/input").send_keys(p)
        driver.find_element_by_xpath("//*[@class='pn pnc']").click()
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/strong/a")))
        driver.get('http://i.pcbeta.com/home.php?mod=task&do=apply&id=149')
        time.sleep(5)
        driver.quit()
        print("ok")
    except Exception as error:
        print(error)
        push('用户名：' + u + '，站点：' + n + '，')


def kafan(u, p, url,n):
    try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input")))
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input").send_keys(u)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div[2]/table/tbody/tr/td[1]/input").send_keys(p)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div/table/tbody/tr/td[1]/button/strong").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/a/img")))
        driver.find_element_by_xpath(
            "/html/body/div/div/div/a/img").click()

        time.sleep(5)
        driver.quit()
        print("ok")
    except Exception as error:
        print(error)
        push('用户名：' + u + '，站点：' +n + '，')


def ruipaike(u, p, url,n):
    try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input")))
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input").send_keys(u)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div[2]/table/tbody/tr/td[1]/input").send_keys(p)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/div[2]/div/div/form/div/div/table/tbody/tr/td[1]/button/strong").click()
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/a")))
        driver.get('https://www.repaik.com/plugin.php?id=dsu_paulsign:sign')
        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/div/form/table[1]/tbody/tr/td/ul/li[@id='kx']/center/img")))
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/form/table[1]/tbody/tr/td/ul/li[@id='kx']/center/img").click()

        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/form/table/tbody/tr/td[1]/input[@id='todaysay']").send_keys("今天又是元气满满的呢！！")

        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/form/table[1]/tbody/tr/td/div/a/img").click()

        time.sleep(5)

        driver.quit()
        print("ok")
    except Exception as error:
        print(error)
        push('用户名：' + u + '，站点：' + n + '，')


def wuai(u, p, url,n):
    try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/form/div/div/p[1]/a/img")))
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/p[1]/a/img").click()
        qqlogin(u,p)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/p[2]/a[1]/img")))
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/p[2]/a[1]/img").click()

        time.sleep(5)
        driver.quit()
        print("ok")
    except Exception as error:
        print(error)
        push('用户名：' + u + '，站点：' + n + '，')




'''macdo('740162752@qq.com', '1357954163', 'https://www.macdo.cn/','Mac毒')
macdo('18051735535@163.com', '1357954163', 'https://www.macdo.cn/','Mac毒')
pcbeta('labulac', 'Aa1357954163', 'http://bbs.pcbeta.com/member.php?mod=logging&action=login','远景')
kafan('740162752','1357954163Cxf','https://bbs.kafan.cn/member.php?mod=logging&action=login','卡饭')
ruipaike('740162752', 'Aa1357954163', 'https://www.repaik.com/member.php?mod=logging&action=login','睿派克')
'''
wuai('740162752','1357954163cxf','https://www.52pojie.cn/','吾爱')