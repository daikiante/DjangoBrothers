from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:pk>/', views.users_detail, name='users_detail'),
]


# MEDIA_ROOTを公開する
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)