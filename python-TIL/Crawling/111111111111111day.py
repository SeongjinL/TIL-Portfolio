key = '4e6976457a617a6138354872675665'
spot = 'D-42'
url = f'http://openapi.seoul.go.kr:8088/{key}/xml/VolInfo/1/8/{spot}/20210702/18/'

import requests
import xmltodict

response = requests.get(url)
response.text
result = xmltodict.parse(response.text)
result['VolInfo']['RESULT']['CODE']

traffic = {}
for day in range(1, 32):
    for hour in range(0, 24):
        url = f'http://openapi.seoul.go.kr:8088/{key}/xml/VolInfo/1/8/{spot}/202107{day:02}/{hour:02}/'
        response = requests.get( url )
        result = xmltodict.parse( response.text )
        status = result['VolInfo']['RESULT']['CODE']
        if status == 'INFO-000':
            vol = 0
            for row in result['VolInfo']['row']:
                vol += int( row['vol'])
                dt = '{}-{}-{:02}'.format( row['ymd'][4:6], row['ymd'][6:], int(row['hh']) + 1)
                traffic[dt] = vol
        else:
            dt = '{}-{}-{:02}'.format( row['ymd'][4:6], row['ymd'][6:], int(row['hh']) + 1)
            traffic[dt] = 0