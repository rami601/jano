from re import M
from django.shortcuts import render
from django.http import HttpResponse
from calendar import HTMLCalendar, month_name
import calendar
from datetime import datetime
# Create your views here.

guest = "rami"
yeaer = " we are in 2022"

def say_hi(request):

    return render(request,"playground/index.html",{"the_guest":guest})
def test(request):

    return render(request,"playground/test.html")

def year(request,years,month):
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_time  = now.strftime('%I: :%M %p ')
    current_month = int(current_month)
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    cal = HTMLCalendar().formatmonth(current_year,current_month)
    return render(request,"playground/index.html",{"current_time":current_time,"years":current_year,"month_number":month_number,"cal":cal})
