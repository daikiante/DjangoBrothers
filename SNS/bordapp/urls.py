from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'bordapp'
urlpatterns = [
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('list/', views.listfunc, name='list'),
    path('logout/', views.logoutfunc, name='logout'),
    path('detail/<int:pk>', views.detailfunc, name='detail'),
    path('good/<int:pk>', views.goodfunc, name='good'),
    path('read/<int:pk>', views.readfunc, name='read'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)