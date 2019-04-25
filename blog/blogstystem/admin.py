from django.contrib import admin

from .models import Users,Article,Ladel,Comment,Fei

# Register your models here.
# class Usersline(admin.StackedInline):
#     model = Users
#     # 关联个数
#     extra = 2
#
# class Articleline(admin.StackedInline):
#     model = Article
#     extra = 2
#
#
#
# class ArticleAdmin(admin.ModelAdmin):
#     inlines = [Usersline]
#
# class LadelAdmin(admin.ModelAdmin):
#     inlines = [Articleline]
#
# class CommentAdmin(admin.ModelAdmin):
#     inlines = [Usersline]
#     inlines = [Articleline]




admin.site.register(Users)
admin.site.register(Article)
admin.site.register(Ladel)
admin.site.register(Comment)
admin.site.register(Fei)