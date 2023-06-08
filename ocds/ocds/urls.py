# from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from ocds import views
from . import views

urlpatterns = [
    path('', views.lecture_list, name ='lecture_list'),
    path('lecture_play/', views.lecture_play, name ='lecture_play'),
    path('detectme', views.detectme, name="detectme"),
    path('lecture_sort/', views.lecture_sort, name='lecture_sort'),
    path('check_user_info/', views.check_user_info, name='check_user_info'),
    path('get_lecture_name/', views.get_lecture_name, name='get_lecture_name'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)