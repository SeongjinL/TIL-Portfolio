from urllib.request import AbstractDigestAuthHandler
from itsdangerous import json
import pymysql
from sklearn.cluster import k_means
from sqlalchemy import create_engine
from sympy import Q, as_finite_diff, sec
import settings
import requests
import datetime
from query import Query 
from datetime import timedelta
import pandas as pd
from pandas.io.json import json_normalize
import json
import sys
import math


class Crawler():
    bearer_token = "AAAAAAAAAAAAAAAAAAAAANBuZQEAAAAAlevil2XBPe8QPX38bCqNL9a6wXI%3DgYGpD9PYq7SeOxU7UqC8ekGHk6pYSDQaQAK3mA0GLALHSpCwgh"
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    # keyword, #hashtag, is-retweet=True/False
    api_query = None
    # 기간설정 한국 시간으로 설정하면 알아서 utc+09:00으로 변환되서 들어감
    start = None
    # 현재시간 기준으로 설정하지만 api는 현재 시간 10초 이전의 것만 받아올수 있음
    end = None
    period = None

    def bearer_oauth(self, r):
        """
        Method required by bearer token authentication.
        """
        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r

    def connect_to_endpoint(self, url, params):
        response = requests.get(url, auth=self.bearer_oauth, params=params)
        #print(response.status_code)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        return response.json()
    
    def printProgress (self, iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100): 
        formatStr = "{0:." + str(decimals) + "f}" 
        percent = formatStr.format(100 * (iteration / float(total))) 
        filledLength = int(round(barLength * iteration / float(total))) 
        bar = '#' * filledLength + '-' * (barLength - filledLength) 
        sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)), 
        if iteration == total: 
            sys.stdout.write('\n') 
        sys.stdout.flush()

    def connect_to_db() :
        try:
            result = pymysql.connect(
                user = settings.DATABASES['default']['USER'],
                passwd=settings.DATABASES['default']['PASSWORD'],
                host=settings.DATABASES['default']['HOST'],
                db=settings.DATABASES['default']['NAME'],
                charset=settings.DATABASES['default']['charset']
                )
            print("connected to " + settings.DATABASES['default']['NAME'] +"DB")
        except:
            print("fail to connect to server")

        cursor = result.cursor(pymysql.cursors.DictCursor)

        return result, cursor

    # query와 시작시간 끝나는 시간 datetime 타입으로 받아옴
    def search(self, query, start, end, dataFrame):
        
        #datetime 타입을 포맷에 맞는 str타입으로 변환
        start_str = start.strftime("%Y-%m-%dT%H:%M:%S+09:00")
        end_str = end.strftime("%Y-%m-%dT%H:%M:%S+09:00")
        
        #query_param 생성
        query_params = { 'start_time' : start_str ,'end_time' : end_str,'query': query,'expansions':'author_id', 
    'tweet.fields': 'author_id,created_at','user.fields': 'username','max_results' : 100}

        #생성된 query_param 으로 api 호출
        json_response = self.connect_to_endpoint(self.search_url, query_params)
        if 'data' in json_response :
            df = pd.json_normalize(json_response,'data')
            df2 = pd.json_normalize(json_response['includes'],'users')
            df2.rename(columns={'id' : 'author_id'}, inplace=True)
            df = pd.merge(df2, df, on='author_id', how='left')
            dataFrame = pd.concat([dataFrame,df], ignore_index=True)

        return dataFrame

    def search_period(self, start, end, period, api_query) :
        dataFrame = pd.DataFrame(index= range(0,0), columns=['name','text','created_at'])
        
        total = math.ceil((end - start) / period)
        i = 0
        self.printProgress(0, total, 'Progress:', 'Complete', 1, 50)
        while(start < end) :
            temp_end = start + period
            if (temp_end > end) : 
                temp_end = end
                
            dataFrame = self.search(api_query,start,temp_end,dataFrame)
            start += period
            i+=1
            self.printProgress(i, total, 'Progress:', 'Complete', 1, 50)
        return dataFrame


    def run(self, table_name) :
        print(self.start , "와" , self.end, "사이에 생성된 트윗들을\n", self.period, "간격으로 크롤링합니다")
        df = self.search_period(self.start,self.end,self.period,self.api_query)
        print("총 ", len(df.index), "개의 트윗이 dataframe에 저장되었습니다")
        print("DB에 저장?(y/n) :",end='')
        ans = input()

        if ans == "y":
            db_connection_str = 'mysql+pymysql://'+settings.DATABASES['default']['USER']+':'+settings.DATABASES['default']['PASSWORD']+'@'+settings.DATABASES['default']['HOST']+'/'+settings.DATABASES['default']['NAME']
            db_connection = create_engine(db_connection_str)
            conn = db_connection.connect()
            df.to_sql(name=table_name, con=db_connection, if_exists='append',index=False)  

        else:
            print("ㄴㄴ")
        return(df)

    def __init__(self, query, start, end, period) :
        
        self.api_query = query
        self.start = start
        self.end = end
        self.period = period