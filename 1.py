import time
import requests
import json
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def cccccc(a):
    cc = ''

    for cookie in a:
        c = str('"%s"''=''"%s";' % (cookie['name'], cookie['value']))

        cc = cc + c
        print("'%s'='%s'" % (cookie['name'], cookie['value']))

    # for i in range(len(ccccc)):

    print(cc)
    return cc


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


def get(u, c, n):
    headers = {
        "Cookie": c,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1"
    }

    a = requests.get(u, headers=headers)
    time.sleep(10)

    b = requests.get(u, headers=headers)
    print(a.content.decode('unicode_escape'))

    if a.text == b.text:
        push(n)


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


def macdo(u, p, url, n):
    attempts = 0
    little = 0
    success = False
    while attempts < 4 and not success:
        time.sleep(5)
        driver = webdriver.Chrome(chrome_options=option)
        try:
            print(n + '开始')

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
            print('用户名：' + u + '，站点：' + n + "ok")
            success = True
        except Exception as error:
            print(error)
            driver.quit()
            attempts += 1
            print('第' + str(attempts) + '次大尝试')
            if attempts == 4:
                push('用户名：' + u + '，站点：' + n + '，')
                success = True


def pcbeta(u, p, url, n):
    attempts = 0
    little = 0
    success = False
    while attempts < 4 and not success:
        time.sleep(5)
        driver = webdriver.Chrome(chrome_options=option)
        try:
            print(n + '开始')

            driver.get(url)
            print('开始查找输入框')
            WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input")))
            print('开始输入u')

            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input").send_keys(u)
            print('开始输入p')
            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/div[2]/div/div/form/div/div[2]/table/tbody/tr/td[1]/input").send_keys(p)
            WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                (By.XPATH, "//*[@class='pn pnc']/strong")))

            print('点击登录')
            driver.find_element_by_xpath("//*[@class='pn pnc']/strong").click()

            print('等等30s')
            time.sleep(30)

            '''
               driver.get('http://i.pcbeta.com/')
                cookies = driver.get_cookies()
                print(cookies)
    
                cookie = cccccc(cookies)
    
                url2 = "http://i.pcbeta.com/home.php?mod=task&do=apply&id=149"
    
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-Hans-CN,zh-CN;q=0.9,zh;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,af;q=0.4',
                    'Cache-Control': 'no-cache',
                    'Cookie': cookie,
                    'dnt': '1',
                    'Host': 'bbs.pcbeta.com',
                    'Pragma': 'no-cache',
                    'Proxy-Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Mobile Safari/537.36'
                }
    
                requests.get(url2, headers=headers)
                time.sleep(3)
                r = requests.get(url2, headers=headers)
                print(r.text)
                '''

            print('查找退出')
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/a[8]")))
            '''print('点击任务')
            driver.find_element_by_xpath("/html/body/div/div/div/div/a[@class='new']").click()
            print('查找签到')
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/table/tbody/tr/td[2]/a/img")))
            print('点击签到')
            driver.find_element_by_xpath("/html/body/div/div/div/div/div/table/tbody/tr/td[2]/a/img").click()
            print('签到')'''
            driver.get('http://i.pcbeta.com/home.php?mod=task&do=apply&id=149')
            print('源码')
            source = driver.page_source
            print(source)

            if ("本期您已申请过此任务" in source):

                driver.quit()
                print('用户名：' + u + '，站点：' + n + "ok")
                success = True
            elif ("您需要先登录才能继续本操作" in source):
                driver.quit()
                little += 1
                print('第' + str(little) + '次小尝试')
                if little == 4:
                    push('用户名：' + u + '，站点：' + n + '，')
                    success = True



        except Exception as error:
            print(error)
            driver.quit()
            attempts += 1
            print('第' + str(attempts) + '次大尝试')
            if attempts == 4:
                push('用户名：' + u + '，站点：' + n + '，')


def pcbetanew(u, n):
    print(n + '开始')

    url1 = 'http://i.pcbeta.com/home.php?mod=task&do=apply&id=149'
    url2 = 'http://i.pcbeta.com/home.php?mod=task&do=draw&id=149'

    cookie = 'Hm_lpvt_76c941eab16e9b48cd0fb4a6d9482a4f=1587615363; Hm_lvt_76c941eab16e9b48cd0fb4a6d9482a4f=1587075355,1587353237,1587594092,1587615362; jqCP_887f_lastact=1587615363%09home.php%09task; jqCP_887f_sid=qfcDB8; jqCP_887f_uuid=4861988; _ga=GA1.2.199150614.1586567700; _gid=GA1.2.654003139.1587594076; jqCP_887f_checkpm=1; jqCP_887f_mobile=no; jqCP_887f_mrd=%09; jqCP_887f_sendmail=1; jqCP_887f_auth=50faOh8s9r%2F37oWeL0HOi8Gf8zLjuk6Gd6DR2xf8uoNaK8cysPA%2BDsqntMsk5oYHnsDAyNfxCE9qOD8akNUWaD5fIuOm; _gat=1; jqCP_887f_ulastactivity=1384GXJ7oWZKvVe28nI8p2httMkaleLcvrkmwkh4ztPXt1Bn2TYH; jqCP_887f_lastvisit=1587343845; jqCP_887f_saltkey=waA2QsJs'

    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Mobile/15E148 Safari/604.1"}

    try:
        requests.get(url1, headers=headers)
        time.sleep(10)

        html = requests.get(url1, headers=headers).text
        # print(html)

        if ("本期您已申请过此任务" in html) or ("成功" in html):

            h = requests.get(url2, headers=headers).text

            if ("收到奖励通知" in h) or ("不是进行中的任务" in h):
                print('用户名：' + u + '，站点：' + n + "ok")

        else:

            push('用户名：' + u + '，站点：' + n + ',cookie失效，')




    except Exception as error:
        print(error)
        print('行号', error.__traceback__.tb_lineno)


def kafan(u, p, url, n):
    attempts = 0
    little = 0
    success = False
    while attempts < 4 and not success:
        time.sleep(5)
        driver = webdriver.Chrome(chrome_options=option)
        try:
            print(n + '开始')

            driver.get(url)

            WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input")))
            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/div[2]/div/div/form/div/div[1]/table/tbody/tr/td[1]/input").send_keys(u)
            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/div[2]/div/div/form/div/div[2]/table/tbody/tr/td[1]/input").send_keys(p)
            driver.find_element_by_xpath(
                "/html/body/div/div/div/div/div[2]/div/div/form/div/div/table/tbody/tr/td[1]/button/strong").click()
            WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/a/img[@class='qq_bind']")))
            driver.find_element_by_xpath("/html/body/div/div/div/a/img[@class='qq_bind']").click()

            time.sleep(5)
            driver.quit()
            print('用户名：' + u + '，站点：' + n + "ok")
            success = True
        except Exception as error:
            print(error)
            driver.quit()
            attempts += 1
            print('第' + str(attempts) + '次大尝试')
            if attempts == 4:
                push('用户名：' + u + '，站点：' + n + '，')
                success = True


def ruipaike(u, p, url, n):
    attempts = 0
    little = 0
    success = False
    while attempts < 4 and not success:
        time.sleep(5)

        driver = webdriver.Chrome(chrome_options=option)
        try:
            print(n + '开始')

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
            print('用户名：' + u + '，站点：' + n + "ok")
            success = True
        except Exception as error:
            print(error)
            driver.quit()
            attempts += 1
            print('第' + str(attempts) + '次大尝试')
            if attempts == 4:
                push('用户名：' + u + '，站点：' + n + '，')
                success = True


def wuai(n):
    '''try:
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(url)

        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div/div/form/div/div/p[1]/a/img")))
        driver.find_element_by_xpath("/html/body/div/div/div/form/div/div/p[1]/a/img").click()

        # qq登录区
        WebDriverWait(driver, 60).until(EC.presence_of_element_located(
            (By.XPATH, ".//*[@id='ptlogin_iframe']")))
        iframe = driver.find_element_by_xpath(".//*[@id='ptlogin_iframe']")
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath(".//*[@id='switcher_plogin']").click()
        driver.find_element_by_xpath(".//*[@id='u']").send_keys(u)
        driver.find_element_by_xpath(".//*[@id='p']").send_keys(p)
        driver.find_element_by_xpath(".//*[@id='login_button']").click()
        # qq登录结束区
        iframe = driver.find_element_by_xpath(".//*[@id='ptlogin_iframe']")
        driver.switch_to.frame(iframe)
        button = driver.find_element_by_id('tcaptcha_drag_button')  # 寻找滑块
        print("寻找滑块")

        time.sleep(1)

        print("开始拖动")
        distance = 175
        action = ActionChains(driver)
        action.reset_actions()
        action.click_and_hold(button).perform()
        action.move_by_offset(distance, 0).perform()
        action.release().perform()




        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/p[1]/strong/a")))
        driver.get('https://www.52pojie.cn/home.php?mod=task&do=apply&id=2')
        time.sleep(5)
        driver.quit()
        print("ok")
    except Exception as error:
        print(error)
        push('用户名：' + u + '，站点：' + n + '，')'''  # 模拟登录，最好在国内QQ
    time.sleep(5)
    print(n + '开始')

    cookie = 'Hm_lpvt_46d556462595ed05e05f009cdafff31a=1585824773; Hm_lvt_46d556462595ed05e05f009cdafff31a=1585824632,1585824729; htVD_2132_auth=c4d6Q7LNab2YubOlE5xkTt9Ie%2FcleP1BTK15VPQXROs1jxa4JL03csuTPZKn6WiE5Xdy3ydYu5X3qESrhjvaMi%2FkaHk; htVD_2132_checkfollow=1; htVD_2132_checkpm=1; htVD_2132_client_created=1585824767; htVD_2132_client_token=0CCAC93F86CF62B2AADDEFFA6E1BE5B3; htVD_2132_connect_is_bind=1; htVD_2132_connect_login=1; htVD_2132_connect_uin=0CCAC93F86CF62B2AADDEFFA6E1BE5B3; htVD_2132_lastact=1585824768%09home.php%09spacecp; htVD_2132_lastcheckfeed=689288%7C1585824768; htVD_2132_stats_qc_login=3; htVD_2132_ttask=689288%7C20200402; htVD_2132_ulastactivity=1585824767%7C0; htVD_2132_con_request_uri=https%3A%2F%2Fwww.52pojie.cn%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dhttps%253A%252F%252Fwww.52pojie.cn%252F; htVD_2132_seccode=1516986.7c17cd1df34d2d3aac; __gads=ID=b387dfa2869a213e:T=1585824634:S=ALNI_MbbPJ1pCgZBXmO-KbRBsSnSBuKtPQ; htVD_2132_lastvisit=1585821029; htVD_2132_saltkey=J2iiPTBi'

    url1 = "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2"
    url2 = "https://www.52pojie.cn/home.php?mod=task&do=draw&id=2"

    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36"
    }

    try:
        requests.get(url1, headers=headers)
        requests.get(url2, headers=headers)
        r = requests.get(url1, headers=headers)
        r2 = requests.get(url2, headers=headers)

        if (r.text.find("六个核的桃") == -1) or (r2.text.find("六个核的桃") == -1):
            print("???")
            push('cookie失效，' + n)
        else:
            print(n + "ok!!!")
    except Exception as e:
        print(e)


def tianyi(n):
    url1 = 'https://api.cloud.189.cn/mkt/userSign.action?clientType=TELEIPHONE&version=8.5.4&model=iPhone&osFamily=iOS&osVersion=12.4&clientSn=9C3FED06-D5E8-4A15-BEA4-390218BE5682'
    headers1 = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip",
        "Accept-Language": "zh-cn",
        "Connection": "close",
        "Cookie": "JSESSIONID=aaabqAey1eSjD9cfAjWgx",
        "Date": "Wed, 29 Apr 2020 15:43:03 GMT",
        "Host": "api.cloud.189.cn",
        "Signature": "f2d3422fbb8789f6ac387ecd7a2904bd2f13b1aa",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Ecloud/8.5.4 (iPhone; 9C3FED06-D5E8-4A15-BEA4-390218BE5682; appStore) iOS/12.4",
        "X-Request-ID": "CCAC08E1C3A64857B3A75EDC6508B467",
        "sessionKey": "d7d9f24e-289c-4e9a-8f81-9336ce8ee95b",
    }

    r = requests.get(url1, headers=headers1).text

    url2 = 'https://m.cloud.189.cn/v2/drawPrizeMarketDetails.action?taskId=TASK_SIGNIN&activityId=ACT_SIGNIN&noCache=0.5006331816484536'

    headers2 = {
        "Accept": "*/*",
        "Accept-Encoding": "br, gzip, deflate",
        "Accept-Language": "zh-cn",
        "Connection": "close",
        "Cookie": "COOKIE_LOGIN_USER=2DE7146F6D3627160ED15007AB19BCC2485815921574448B96BE30F8D7E669FE33145EF94A575C06BF99FCE72E3CC6E2E557C90F1096E4A72DC5636F; JSESSIONID=aaaHQl3caJ5ZGa9KBibhx; apm_ct=20200430000737325; apm_ip=58.219.213.96; apm_sid=4950972F722D0388761F5AE28EEA2F88; apm_ua=A40A13758A14B9205A83415498CE3559; apm_uid=C5A059FFD18E75743D4141FB4B318ACB",
        "Host": "m.cloud.189.cn",
        "Referer": "https://m.cloud.189.cn/zhuanti/2016/sign/index.jsp?albumBackupOpened=0",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Ecloud/8.5.4 iOS/12.4 clientId/9C3FED06-D5E8-4A15-BEA4-390218BE5682 clientModel/iPhone proVersion/1.0.5",
        "X-Requested-With": "XMLHttpRequest",
        "Signature": "f2d3422fbb8789f6ac387ecd7a2904bd2f13b1aa",
        "sessionKey": "083a7824-8c6e-429d-8c5d-2c898abdbbb6",
    }

    h = requests.get(url2, headers=headers2).text
    print(h)

    if ("获得" in r):
        print('天翼云盘首页签到：' + "ok")
    else:
        push(n + '首页签到：')

    if ("空间" in h):
        print('天翼云盘额外领取：' + "ok")
    else:
        push(n + '额外领取：')
        
        
def suchengma(n):
    url='https://sct.szgaj.cn/integralApi/sign'
    data={"Accept": "application/json, text/plain, */*","Accept-Encoding": "br, gzip, deflate","Accept-Language": "zh-cn","Authorization": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODA1MTczNTUzNSIsImNyZWF0ZWQiOjE1OTA3NDE0NDE4MDQsImV4cCI6MTU5MTE3MzQ0MX0.vClpDgp8Gav7w4nCwIBOkt_ZjZUc8jFvmSexiIMKJVvQ9zHNb2frmrybScEuaCM0FOLYXPap6NqLX7FyXG8Qcg","Connection": "close","Content-Type": "application/x-www-form-urlencoded","Cookie": "SERVERID=c6ad355529ef561b1ed4b9aef69f94e8|1590741554|1590741554; Hm_lvt_d658bea862b5c5a67b2e9d308649bd27=1590741480","Host": "sct.szgaj.cn","Origin": "https://sct.szgaj.cn","Referer": "https://sct.szgaj.cn/integral/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",}
    r =requests.post(url,data)
    print(r.text)
    print(r.status_code)
    if r.status_code != 200:
        push (n)

suchengma('苏城码')
# tianyi('天翼云盘')
pcbetanew('labulac', '远景')
macdo('740162752@qq.com', '1357954163', 'https://www.macdo.cn/', 'Mac毒')
macdo('18051735535@163.com', '1357954163', 'https://www.macdo.cn/', 'Mac毒')
#kafan('740162752', '1357954163Cxf', 'https://bbs.kafan.cn/member.php?mod=logging&action=login', '卡饭')
wuai('吾爱')
# ruipaike('740162752', 'Aa1357954163', 'https://www.repaik.com/member.php?mod=logging&action=login', '睿派克')

