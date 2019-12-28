from django.urls import path
from . import views


app_name = 'bordapp'
urlpatterns = [
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    
]
