from django.db import models

from blogstystem.models import Article

# Create your models here.
#
#
# class Commenta(models.Model):
#     crname=models.CharField(max_length=20,blank=True)
#     cemail=models.EmailField(blank=True)
#     chttp=models.CharField(max_length=30,blank=True)
#     cname=models.TextField()
#     ctime=models.DateTimeField(auto_now_add=True)  #时间
#     carticle_id=models.ForeignKey(Article,on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.cname