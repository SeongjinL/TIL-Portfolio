from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\\Users\\sung\\Desktop\\file\\chromedriver.exe")
browser = webdriver.Chrome(service=service)

url = ''

