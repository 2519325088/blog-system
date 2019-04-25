from django.shortcuts import render,redirect,reverse

from django.http import HttpResponse,HttpResponseRedirect

from .models import Users,Article,Ladel,Comment,Fei

import datetime

# Create your views here.


# 首页
def index(request):
    wz=Article.objects.all()
    bq=Ladel.objects.all()
    lei=Fei.objects.all()
    now_time=datetime.datetime.now()
    zxwz=Article.objects.order_by('-atime')[:3]
    gd=Article.objects.dates("atime", "month", order="DESC")[:3]
    return render(request,'demo1/index.html',{'wz':wz,'bq':bq,'lei':lei,'zxwz':zxwz,'ntime':now_time,'gd':gd})


#归档
def gd(request,y,m):
    wz=Article.objects.filter(atime__year=y,atime__month=m)
    bq = Ladel.objects.all()
    lei = Fei.objects.all()
    now_time = datetime.datetime.now()
    zxwz = Article.objects.order_by('-atime')[:3]
    gd = Article.objects.dates("atime", "month", order="DESC")[:3]
    return render(request,'demo1/gd.html',{'wz':wz,'bq':bq,'lei':lei,'zxwz':zxwz,'ntime':now_time,'gd':gd})


# 分类
def leibie(request,id):
    lx=Fei.objects.get(pk=id)
    print(lx)
    wz=lx.article_set.all()
    print(len(wz))
    bq = Ladel.objects.all()
    lei = Fei.objects.all()
    now_time = datetime.datetime.now()
    zxwz = Article.objects.order_by('-atime')[:3]
    gd = Article.objects.dates("atime", "month", order="DESC")[:3]
    return render(request,'demo1/leibie.html',{'wz':wz,'bq':bq,'lei':lei,'zxwz':zxwz,'ntime':now_time,'gd':gd})


#标签
def bqian(request,id):
    lx=Ladel.objects.get(pk=id)
    print(lx)
    wz=lx.article_set.all()
    print(len(wz))
    bq = Ladel.objects.all()
    lei = Fei.objects.all()
    now_time = datetime.datetime.now()
    zxwz = Article.objects.order_by('-atime')[:3]
    gd = Article.objects.dates("atime", "month", order="DESC")[:3]
    return render(request,'demo1/bqian.html',{'wz':wz,'bq':bq,'lei':lei,'zxwz':zxwz,'ntime':now_time,'gd':gd})

# 详情
def single(request,id):
    wz=Article.objects.get(pk=id)
    wz.apageview+=1
    wz.save()
    bq=wz.larticle_id.all()
    now_time = datetime.datetime.now()
    lei = Fei.objects.all()
    zxwz = Article.objects.order_by('-atime')[:3]
    gd = Article.objects.dates("atime", "month", order="DESC")[:3]
    return render(request,'demo1/single.html',{'wz':wz,'zxwz':zxwz,'lei':lei,'bq':bq,'ntime':now_time})


def fullw(request):
    return render(request, 'demo1/full-width.html')


def about(request):
    return  render(request,'demo1/about.html')


def contact(request):
    return  render(request,'demo1/contact.html')
