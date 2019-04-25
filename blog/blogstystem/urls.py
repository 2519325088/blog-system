from django.conf.urls import url,include

from . import views

app_name='blogstystem'

urlpatterns = [
    #首页
    url(r'^$',views.index,name='index'),
    #分类
    url(r'^leibie/(\d+)/$',views.leibie,name='leibie'),
    #标签
    url(r'^bqian/(\d+)/$',views.bqian,name='bqian'),
    #归档
    url(r'^gd/(\d+)/(\d+)/$',views.gd,name='gd'),
    #详情
    url(r'^single/(\d+)/$',views.single,name='single'),

    url(r'^fullw/$',views.fullw,name='fullw'),
    #关于
    url(r'^about/$',views.about,name='about'),

    url(r'^contact/$',views.contact,name='contact'),

]