from django.contrib import admin
from App_Blog.models import Blog,BlogCatagory
# Register your models here.

admin.site.register(BlogCatagory)
admin.site.register(Blog)