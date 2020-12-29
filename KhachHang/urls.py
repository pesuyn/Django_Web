from django.contrib import admin
from django.urls import path,include
from . import views
from .views import add_to_cart, ChiTietSP


app_name = 'trang-chu'
urlpatterns = [
    path('dangnhap/', views.dangnhap.as_view(), name='dangnhap'),
    path('product/<slug>/', ChiTietSP.as_view(), name='product'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('',views.Trangchu.as_view(),name='trangchu' ),
    path('thanhtoan/',views.thanhtoan.as_view(),name='thanhtoan' ),
    path('giohang/',views.giohang.as_view(),name='giohang' ),
    path('tintuc/',views.tintuc.as_view(),name='tintuc' ),


]
