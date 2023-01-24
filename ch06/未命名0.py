import requests
import os
from io import StringIO
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import crawler_module as m
from time import sleep
import mpl_finance as mpf
import talib

def get_setting():
    listt = []
    with open('setting.csv') as f:  
        data = f.readlines()
        print('讀入：',data)
        start_day, end_day, number = data[0].split(',')
        listt = [start_day, end_day, number]
        f.close()
    return listt

def get_time():
    day = []
    setting = get_setting()
    start_day = datetime.datetime.strptime(setting[0], '%Y%m%d')
    end_day = datetime.datetime.strptime(setting[1], '%Y%m%d')
    for time in range((end_day - start_day).days + 1):
        day.append((start_day + datetime.timedelta(days=time)).strftime('%Y%m%d'))
    return setting[2], day
def get_document(date, symbol):
    # 下載股價
    file = requests.get(
        'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date='+ date + '&type=ALL')

    file_csv = [i for i in file.text.split('\n') if len(i.split('",')) == 17 and i[0] != '=']
    print(file_csv)
    df = pd.read_csv(StringIO("\n".join(file_csv)), header=0)
    df = df.drop(columns=['Unnamed: 16'])
    filter_df = df[df["證券代號"] == symbol]
    filter_df.insert(0, "日期", date)
    return list(filter_df.iloc[0]), filter_df.columns

predict_stock_list = []
stock_number, time = get_time()
for time_number in time:
    sleep(1.5)
    try:
        temp_data = get_document(time_number, stock_number)
        predict_stock_list.append(temp_data[0])
        columns = temp_data[1]
        print(predict_stock_list)
        print(columns)
        print(temp_data)
        print("  OK!  time = " + time_number + " ,stock symbol = " + stock_number)
    except:
        print("error! time = " + time_number + " ,stock symbol = " + stock_number)

