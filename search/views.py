from django.shortcuts import redirect, render, get_object_or_404
from .models import search
import requests
import sqlite3 
from datetime import datetime
import time


# Create your views here.
def inputForm(request):
    return render(request, 'base.html')


def search(request, name, start_date, end_date):
    interval='1d'
    #연월일을 초로 변환
    start_date2 = from_yyyymmdd_to_second(start_date)
    end_date2 = from_yyyymmdd_to_second(end_date)
    
    # 여기다가 주가데이터 call 후에 db에 저장
    link="https://query1.finance.yahoo.com/v7/finance/download/"+str(name)+"?period1="+str(start_date2)+"&period2="+str(end_date2)+"&interval="+interval+"&events=history";
    
    print(link)
    
    response = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
    
    print(response)
    decoded_response = response.content.decode('ascii')
    result_list = decoded_response.split('\n')
    final = list(map(lambda x:x.split(','), result_list))

    #db import 
    init_db(final)
    print("finished init db:>>>>")
    return redirect('https://localhost:8080/stocks')


def from_yyyymmdd_to_second(str_date):
    input_date = str(str_date)+" 00:00:00"
    d = datetime.strptime(input_date, "%Y%m%d %H:%M:%S")
    return str(time.mktime(d.timetuple())).split(".")[0]

def init_db(final):
    data = final
    conn = sqlite3.connect('stock.db', detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    sql = "INSERT INTO 'stock' (date, open, high, low, close, adj_close, volume) VALUES (?, ?, ?, ?, ?, ?, ?);"
    for stock in data:
        cursor.execute(sql, stock)
    cursor.commit()
    conn.close()