from django.db import models

# Create your models here.

# 用户
class Users(models.Model):
    uname=models.CharField(max_length=21)
    upasswd = models.CharField(max_length=21)

    def __str__(self):
        return self.uname

# 文章
class Article(models.Model):
    aname=models.CharField(max_length=90)  #名字
    acontent=models.TextField()  #内容
    atime=models.DateTimeField(auto_now_add=True)    #创建时间
    axtime=models.DateTimeField(auto_now_add=True)  #修改时间
    apageview=models.IntegerField(default=0) #阅读量
    alei=models.ForeignKey('Fei',on_delete=models.CASCADE)  #分类
    auser_id=models.ForeignKey('Users',on_delete=models.CASCADE)  #用户
    larticle_id = models.ManyToManyField(to='Ladel')  #标签云
    def __str__(self):
        return self.aname

# 分类
class Fei(models.Model):
    fname=models.CharField(max_length=30)

    def __str__(self):
        return self.fname


# 标签
class Ladel(models.Model):
    lname=models.CharField(max_length=60)


    def __str__(self):
        return self.lname

# 评论
class Comment(models.Model):
    crname=models.CharField(max_length=20)
    cemail=models.EmailField(blank=True)
    chttp=models.CharField(max_length=30)
    cname=models.TextField()
    ctime=models.DateTimeField(auto_now_add=True)  #时间
    # cuser_id=models.ForeignKey('Users',on_delete=models.CASCADE)
    carticle_id=models.ForeignKey('Article',on_delete=models.CASCADE)

    def __str__(self):
        return self.cname




