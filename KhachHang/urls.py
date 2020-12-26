from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'trang-chu'
urlpatterns = [
    path('',views.Trangchu.as_view(),name='trangchu' ),
    path('thanhtoan/',views.thanhtoan.as_view(),name='thanhtoan' ),
    path('giohang/',views.giohang.as_view(),name='giohang' ),
    path('tintuc/',views.tintuc.as_view(),name='tintuc' ),


]
