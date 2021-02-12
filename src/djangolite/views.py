from forecast.forms import ContactForm, ForecastForm,FcastAllForm
from django.shortcuts import get_object_or_404, render
from forecast.models import Forecast
from datetime import date,timedelta
import datetime
from django.db.models import Avg, Max, Min, Sum
from django.http import HttpResponseRedirect

def currentf(request):
    d1 = date.today()
    d2 = d1 + timedelta(days=1)
    d3 = d1 + timedelta(days=2)
    d4 = d1 + timedelta(days=3)
    d5 = d1 + timedelta(days=4)
    obj = Forecast.objects.all()
    lg5pct = 0.25

    
    obj2 = obj.aggregate(Sum('day1lbs'))
    obj3 = obj.aggregate(Sum('day2lbs'))
    obj4 = obj.aggregate(Sum('day3lbs'))
    obj5 = obj.aggregate(Sum('day4lbs'))
    #d1ttl = Forecast.objects.filter(Day1lbs > 0)
    # obj2 = obj.aggregate(Sum('totalamount'))
    template_name = 'fcast.html'
    total5 = (lg5pct * obj2['day1lbs__sum']/5)
    total5_2 = (lg5pct * obj3['day2lbs__sum']/5)
    total5_3 = (lg5pct * obj4['day3lbs__sum']/5)
    total5_4 = (lg5pct * obj5['day4lbs__sum']/5)
    #total5_5 = (lg5pct * obj2['day5lbs__sum']/5)
    context = {"forecastOBJ":obj,"d1":d1,"d2":d2,"d3":d3,"d4":d4,"d5":d5,"lbs":obj2,"test1":total5,"test2":total5_2,"test3":total5_3,"test4":total5_4}


    return render(request,template_name,context)


def fcastedit(request):
    # i = 0
    # formz = []
    # obj = get_object_or_404(Forecast,roomno = room)
    # obj2 = get_object_or_404(Forecast,roomno = 88)
    obj3 = Forecast.objects.all()
    
    # while i < len(obj3):
    #     fz = ForecastForm(request.POST or None,instance=obj3[i])
    #     formz.append(fz)
    #     i += 1


    if request.method == 'POST':
        d1update= request.POST.get('day1')
        d2update= request.POST.get('day2')
        d3update= request.POST.get('day3')
        onetosave = Forecast.objects.get(roomno = request.POST.get('roomno'))
        onetosave.day1lbs = d1update
        onetosave.day2lbs = d2update
        onetosave.day3lbs = d3update

        onetosave.save()
        return HttpResponseRedirect("/fcast/all")
    template_name = 'update.html'
    context = {'obj3':obj3}
    return render(request,template_name,context)


def addroom(request):
    roomtoadd = request.POST.get('addme')
    print(roomtoadd)
    obj = Forecast.objects.create(roomno = roomtoadd)
    form = ForecastForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'update.html'
    context = {'form':form}
    return render(request,template_name,context)

def fcastall(request):
    #obj = Forecast.objects.all()
    form = FcastAllForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    template_name = 'form2.html'
    context = {'newform':form}
    return render(request,template_name,context)
