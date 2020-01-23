from django.urls import path 

from . import views

urlpatterns = [
    path('personal/',views.home, name='personal-home'),
    path('personal/about',views.about, name='personal-about'),
    path('personal/contact',views.contact, name='personal-contact'),
    path('personal/service',views.service, name='personal-service'),
    path('personal/testimonials',views.testimonials, name='personal-testimonials'),
    
]


