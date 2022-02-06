#두번째 실습
import requests
import bs4

url = ''
response = requests.get(url)
html = bs4.BeautifulSoup( response.text, 'html.parser')

elements = html.select('div#VIPReview')
print(elements)