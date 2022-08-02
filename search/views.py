from django.shortcuts import redirect, render, get_object_or_404
from .models import search
import requests
from datetime import datetime
import time
from stocks.models import stock


# Create your views here.
def inputForm(request):
    return render(request, 'base.html')


def search2(request, name, start_date, end_date):
    interval='1d'

    search(name=name, start_date=start_date, end_date=end_date).save()
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
    init_db(final[1:])
    print("finished init db:>>>>")
    return redirect('http://127.0.0.1:8000/stocks/')

def search_from_page(request):
    name = request.GET['name']
    start_date = request.GET['start_date']
    end_date = request.GET['end_date']

    search(name=name, start_date=start_date, end_date=end_date).save()
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
    init_db(final[1:])
    print("finished init db:>>>>")
    return redirect('http://127.0.0.1:8000/stocks/')



def from_yyyymmdd_to_second(str_date):
    input_date = str(str_date)+" 00:00:00"
    d = datetime.strptime(input_date, "%Y%m%d %H:%M:%S")
    return str(time.mktime(d.timetuple())).split(".")[0]

def init_db(data):
    for single in data:
        print(str(single[0])+" 00:00:00")
        stock(date=str(single[0])+" 00:00:00",
        open=str(single[1]),
        high=str(single[2]),
        low=str(single[3]),
        close=str(single[4]),
        adj_close=str(single[5]),
        volume=str(single[6])).save()