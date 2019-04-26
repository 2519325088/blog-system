from django.shortcuts import render,redirect,reverse

from django.http import HttpResponse,HttpResponseRedirect

from .models import Users,Article,Ladel,Fei,Comment


# from comment.forms import FormAdd
import datetime
import markdown

from django.core.paginator import Paginator

# Create your views here.


# 首页
def index(request):
    wz=Article.objects.all()

    paginator = Paginator(wz,2)
    pagenum = request.GET.get('page')
    pagenum = 1 if pagenum==None else pagenum
    page=paginator.page(pagenum)

    bq=Ladel.objects.all()
    lei=Fei.objects.all()
    now_time=datetime.datetime.now()
    zxwz=Article.objects.order_by('-atime')[:3]
    gd=Article.objects.dates("atime", "month", order="DESC")[:3]
    return render(request,'demo1/index.html',{'wz':wz,'bq':bq,'lei':lei,'zxwz':zxwz,'ntime':now_time,'gd':gd,'page':page})


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
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc'
    ])
    wz.acontent= md.convert(wz.acontent)
    wz.toc = md.toc
    bq=wz.larticle_id.all()
    now_time = datetime.datetime.now()
    lei = Fei.objects.all()
    zxwz = Article.objects.order_by('-atime')[:3]
    gd = Article.objects.dates("atime", "month", order="DESC")[:3]
    return render(request,'demo1/single.html',{'wz':wz,'zxwz':zxwz,'lei':lei,'bq':bq,'ntime':now_time,'gd':gd})



def comment(request,id):
    wz = Article.objects.get(pk=id)
    wz.apageview +=1
    wz.save()
    cname = request.POST['name']
    cemail = request.POST['email']
    curl = request.POST['url']
    ccoment = request.POST['comment']
    a1 = Comment()
    a1.crname =cname
    a1.cemail =cemail
    a1.chttp =curl
    a1.cname =ccoment
    a1.carticle_id=wz
    a1.save()
    # return  HttpResponse('aa')
    bq = wz.larticle_id.all()
    now_time = datetime.datetime.now()
    lei = Fei.objects.all()
    zxwz = Article.objects.order_by('-atime')[:3]
    gd = Article.objects.dates("atime", "month", order="DESC")[:3]
    return HttpResponseRedirect('/blogstystem/single/'+str(wz.id)+'/', {'wz': wz, 'zxwz': zxwz, 'lei': lei, 'bq': bq, 'ntime': now_time,'gd':gd})




def fullw(request):
    return render(request, 'demo1/full-width.html')


def about(request):
    return  render(request,'demo1/about.html')


def contact(request):
    return  render(request,'demo1/contact.html')
