from django.shortcuts import render,redirect,reverse
# from django.http import HttpResponseRedirect,HttpResponse
# # Create your views here.
# import datetime
#
# from .forms import FormAdd
#
# from blogstystem.models import Article
#
# from .models import Commenta
#
# from blogstystem.models import Users,Article,Ladel,Fei
#
#
# def commenta(request,id):
#     wz = Article.objects.get(pk=id)
#     # post=Article.objects.get(pk=id)
#     if request.method=='POST':
#         comment=FormAdd(request.POST)
#         if comment.is_valid():
#             comment=comment.save(commit=False)
#             comment.post=wz
#             wz.apageview += 1
#             wz.save()
#             cname = request.POST['name']
#             cemail = request.POST['email']
#             curl = request.POST['url']
#             ccoment = request.POST['comment']
#             a1 = Commenta()
#             a1.crname = cname
#             a1.cemail = cemail
#             a1.chttp = curl
#             a1.cname = ccoment
#             a1.save()
#             bq = wz.larticle_id.all()
#             now_time = datetime.datetime.now()
#             lei = Fei.objects.all()
#             zxwz = Article.objects.order_by('-atime')[:3]
#             gd = Article.objects.dates("atime", "month", order="DESC")[:3]
#             return HttpResponseRedirect('/blogstystem/single/'+str(wz.id)+'/', {'wz': wz, 'zxwz': zxwz, 'lei': lei, 'bq': bq, 'ntime': now_time,'gd':gd})
#     else:
#         return HttpResponse("11")
# {% url 'blogstystem:comment' wz.id %}