#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import FinanceDataReader as fdr
import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import datetime
from datetime import date
import sys
fdr.__version__
import schedule
import time
import pytz
from numpyencoder import NumpyEncoder
import telegram
import json


# count = 1

def job():
    # 전역변수 설정
#     global Market_timing
#     global count
#     count += 1
    # 한국시각, 주말 설정
#     now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    today = date.today()
    weekend = today.weekday()
    # 예외시간 설정. 9시 이전 및 15시 이후, 주말에는 알람을 보내지 않음
    while weekend >= 5:
        print(weekend)
    
    # 봇 설정
    API_KEY = '5569257444:AAGV21Ds4fkrxhXkrevkdvQ289vGVcajYTU'
    bot = telegram.Bot(token=API_KEY)
    bot.get_updates()
    public_chat_name = '@MarketTimer_alarm_bot'
#     for i in updates:
#     print(i.message['chat']['id'])
    
    # 코스닥지수
    code = 'KQ11'
    df = fdr.DataReader('KQ11','2022-08').reset_index()
    # 3,5,10 이동평균 딕셔너리에 할당
    df['close_sma3d'] = df['Close'].rolling(3).mean()
    df['close_sma5d'] = df['Close'].rolling(5).mean()
    df['close_sma10d'] = df['Close'].rolling(10).mean()
    # dataframe 재구성
    df2 = df.loc[: ,['Date','Close', 'close_sma3d','close_sma5d','close_sma10d']].iloc[-1:]
    alerts = df2[(df2['Close'] > df2['close_sma3d']) | (df2['Close'] > df2['close_sma5d']) | (df2['Close'] > df2['close_sma10d'])]
    alerts2 = df2[(df2['Close'] < df2['close_sma3d']) & (df2['Close'] < df2['close_sma5d']) & (df2['Close'] < df2['close_sma10d'])]
#     def display(row):
# #         row.to_json(orient='records')
#         print(f" - {row['Date']} Signal 발생! 코스닥_현재가 {row['Close']} 3일이동평균 {row['close_sma3d']:.2f} 5일이동평균 {row['close_sma5d']:.2f} 10일이동평균 {row['close_sma10d']:.2f}")
#     Market_timing = alerts.apply(display, axis=1)
    for index, row in alerts.iterrows():
        z = row['Close']
        a = round(row['close_sma3d'], 2)
        b = round(row['close_sma5d'], 2)
        c = round(row['close_sma10d'], 2)
    # telegram 알람에서 출력하기 위해 datetime64만 json str 형식으로 변환
        row['Date'] = row['Date'].date()
        jsonstr1 = json.dumps(str(row['Date']))
        Market_timing = (f"{jsonstr1} 현재가가 3 or 5 or 10 단순이동평균보다 높습니다 코스닥_현재가 {z} 3일이동평균 {a} 5일이동평균 {b} 10일이동평균 {c}")
        bot.sendMessage(chat_id = public_chat_name, text=Market_timing).chat_id
#             bot.sendMessage(chat_id = '1760120639', text = Market_timing)
    for index, row in alerts2.iterrows():
        z2 = row['Close']
        a2 = round(row['close_sma3d'], 2)
        b2 = round(row['close_sma5d'], 2)
        c2 = round(row['close_sma10d'], 2)
    # telegram 알람에서 출력하기 위해 datetime64만 json str 형식으로 변환
        row['Date'] = row['Date'].date()
        jsonstr2 = json.dumps(str(row['Date']))
        Market_timing2 = (f"{jsonstr2} 현재가가 3 and 5 and 10 단순이동평균보다 낮습니다 코스닥_현재가 {z2} 3일이동평균 {a2} 5일이동평균 {b2} 10일이동평균 {c2}")
        bot.sendMessage(chat_id = public_chat_name, text=Market_timing2).chat_id

# 2 시간 마다 실행
# schedule.every(2).hours.do(job)
schedule.every().day.at("10:00").do(job)
schedule.every().day.at("12:00").do(job)
schedule.every().day.at("14:00").do(job)

print('Start App..')

while True:
    schedule.run_pending()
    time.sleep(1)

