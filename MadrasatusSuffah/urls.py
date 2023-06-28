from django.contrib import admin
from django.urls import path,include 
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App_Home.urls')),
    path('account/',include('App_Login.urls')),
    path('blog/',include('App_Blog.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
