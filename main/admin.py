from django.contrib import admin
from .models import Category, Course, Blog, Comment,Subscriber  
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Subscriber)

