from unittest import FunctionTestCase
from crawler import Crawler
from query import Query
import datetime
from sqlalchemy import create_engine
from tkinter import *

def main () :
    api_query = Query("청년희망적금", "", False)
    # 기간설정 한국 시간으로 설정하면 알아서 utc+09:00으로 변환되서 들어감
    start = datetime.datetime(2022, 2, 18, hour=10, minute=0, second=0, microsecond=0)
    # 현재시간 기준으로 설정하지만 api는 현재 시간 10초 이전의 것만 받아올수 있음
    end = datetime.datetime.now() - datetime.timedelta(seconds=11)
    period = datetime.timedelta(hours=1)
    crawler = Crawler(api_query,start,end,period)
    df = crawler.run("tweet_save")

if __name__ == "__main__":
    main()