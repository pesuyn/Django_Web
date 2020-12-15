from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'trang-chu'
urlpatterns = [
    path('',views.Trangchu.as_view(),name='trangchu' ),

]
