import requests
from fake_useragent import UserAgent

agent = UserAgent()
header = {'User-Agent':agent.chrome}

url = ''

response = requests.get(url, headers=header)
print( response.content )