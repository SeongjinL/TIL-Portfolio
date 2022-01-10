key = '4e6976457a617a6138354872675665'
url = f'http://openapi.seoul.go.kr:8088/{key}/xml/SpotInfo/1/169/'

import requests
import xmltodict

response = requests.get(url)
result = xmltodict.parse(response.text)

len(result['SpotInfo']['row'])

for spot in result['SpotInfo']['row']:
    if spot['spot_nm'] == '테헤란로(선릉역)':
        print( spot['spot_num'] )
        print( spot['spot_nm'])
