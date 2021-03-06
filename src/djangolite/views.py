from forecast.forms import ContactForm, ForecastForm,FcastAllForm
from django.shortcuts import get_object_or_404, render
from forecast.models import Forecast
from datetime import date,timedelta
import datetime
from django.db.models import Avg, Max, Min, Sum
from django.http import HttpResponseRedirect
import json 
import pyodbc
from django.http.response import JsonResponse
from .queries import getQuery,query2,query3


def testodbc(request, cname=""):
    #conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=acct-svr;DATABASE=quickbooks15_opensync2FF;UID=sa;PWD=')
    conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=acct-svr;DATABASE=quickbooks15_opensync2;UID=sa;PWD=')
    c = conn.cursor()   


    customers = []
    itemz = []
    #curs = c.execute(getQuery(cname))
    curs = c.execute(query3)
    res = c.fetchall()
    results = []
    results_c = []
    results_w = []
    crims = []
    whites = []
    d1,d2,d3 = [],[],[]
    columns = [column[0] for column in curs.description]
    for row in res:
        results.append(dict(zip(columns, row)))
    i = 0
    while i < len(results):
        if results[i].get('type') == "Crimini":
            results_c.append(results[i])
            i += 1
        elif results[i].get('type') == "White":
             results_w.append(results[i])
             i += 1
        else:
            i += 1
    dayz = []
    for x in results_c:
        if x['saledate'] in dayz:
            pass
        else:
            dayz.append(x['saledate'])
    # xi = 0
    # while xi < len(results_c):
    for x in results_c:
        if x['saledate'] == dayz[0]:
            d1 += [x]
        elif x['saledate'] == dayz[1]:
            d2 += [x]
        elif x['saledate'] == dayz[2]:
            d3 += [x]
        else:
            pass

    

        
    template_name = 'testodbc.html'
    #context = {'results':customers,'itemz':itemz}
    context = {"resz":results_w, "resz_c":results_c,"day1":d1,"day2":d2,"day3":d3}
    return render(request,template_name,context)


       #if request.method == 'GET':
        #return JsonResponse(results,safe=False)


    ###############WORKING#############################
    # i = 0
    # while i < len(results):
    #     if results[i].get('type') == "Crimini":
    #         crims.append(results[i].get('totalcasez'))
    #         i += 1
    #     elif results[i].get('type') == "White":
    #          whites.append(results[i].get('totalcasez'))
    #          i += 1
    #     else:
    #         i += 1

    # total_crims = 0
    # for i in crims:
    #     total_crims += i

    # total_whites = 0
    # for i in whites:
    #     total_whites += i
  ###############WORKING#############################
    # for index in range(len(results)):
    #     for key in results[index]:
    #         customers.append(results[index]['CustomerRef_FullName'])
    #         itemz.append(results[index]['Name'])

    #if request.method == 'GET':
        #return JsonResponse(results,safe=False)

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
#####################################################################################################################


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
    rmadd = request.POST.get('addroom')
    obj3 = Forecast.objects.all() 
    ###########################################DAY SHIFT###################################################################
    for evt in obj3:
        if evt.shiftupdate != datetime.date.today():
            for rec in obj3:
                rec.day1lbs = rec.day2lbs
                rec.day2lbs = rec.day3lbs
                rec.day3lbs = 0
                rec.eclass = 'not-saved'
                rec.shiftupdate = datetime.date.today()
    ##########################################UPDATING A ROOMS' VALUES######################################################
    if request.method == 'POST' and rmadd == None:
        print(request.POST.get('delcheckbox'))
        d1update= request.POST.get('day1')
        d2update= request.POST.get('day2')
        d3update= request.POST.get('day3')
        onetosave = Forecast.objects.get(roomno = request.POST.get('roomno'))
        onetosave.day1lbs = d1update
        onetosave.day2lbs = d2update
        onetosave.day3lbs = d3update
        onetosave.updated = datetime.date.today()
        onetosave.eclass = 'input-box'
        if request.POST.get('delcheckbox') == None:
            onetosave.save()
        else:
            onetosave.delete()
        
        return HttpResponseRedirect("/fcast/all")

    #########################################ADDING A ROOM###################################################################
    if rmadd:
        Forecast.objects.create(roomno = rmadd,updated = datetime.date.today(),shiftupdate = datetime.date.today())
        rmadd = None
        return HttpResponseRedirect("/fcast/all")

    #########################################################################################################################
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




    
