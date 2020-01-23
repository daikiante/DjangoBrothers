from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('post.urls')),
    path('', include('register.urls')),
    path('', include('personal.urls')),
    
    path('admin/', admin.site.urls),
]