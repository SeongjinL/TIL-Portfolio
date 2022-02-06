from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="c:\\Users\\sung\\Desktop\\file\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(service=service, options=options)

url = 'http://lc.multicampus.com/k-digital/#/login'
browser.get(url)

#time.sleep(2)
#inputs = browser.find_elements(By.CSS_SELECTOR, 'div.input-row-line input')
#loginbutton = browser.find_element(By.CSS_SELECTOR, 'div.btn-row button.login btn')

#inputs[0].send_keys('아이디')
#inputs[1].send_keys('비밀번호')
#loginbutton.click()
time.sleep(10)

# 무한 스크롤
# 초기의 높이
last_height = browser.execute_script('return document.body.scrollHeight')
while True:
    # 스크롤을 아래로 내림
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    # 내용이 로딩되는 동안의 시간
    time.sleep(2)
    
    # 새로 높이
    new_height = browser.execute_script('return document.body.scrollHeight')
    
    # 높이가 이전과 같을 경우 더 이상 내려갈 수 없음
    if new_height == last_height: break
    
    # 기존의 높이를 새로운 높이로 변경하고 다음 회차로 이동
    last_height = new_height
    
articles = browser.find_elements(By.CSS_SELECTOR, 'div.feedlist span article')
for article in articles:
    for content in article.find_elements(By.CSS_SELECTOR, 'span.feedContentBlk span'):
        print( content.text )