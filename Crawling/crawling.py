import requests
from fake_useragent import UserAgent

agent = UserAgent()
header = {'User-Agent':agent.chrome}

url = 'https://image.zdnet.co.kr/2022/01/01/e601fd8d72cc33ca75cd9d41d3315684.jpg'

response = requests.get(url, headers=header)
print( response.content )