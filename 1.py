from selenium import webdriver
url='http://www.labulac.top'
option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option)
driver.get(url)
print(driver.page_source)