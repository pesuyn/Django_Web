from django.contrib import admin
from django.urls import path,include
from . import views
from .views import add_to_cart, ChiTietSP,XemTheoLoai,XemTheoNganh,tintuc,search


app_name = 'trang-chu'
urlpatterns = [
    path('dangnhap/', views.dangnhap.as_view(), name='dangnhap'),
    path('product/<id>/', ChiTietSP.as_view(), name='product'),
    path('add-to-cart/<id>/', views.add_to_cart, name='add-to-cart'),
    path('add-to-cart-1/<id>/', views.add_1, name='add-to-cart-1'),
    path('',views.Trangchu.as_view(),name='trangchu'),
    path('thanhtoan/',views.thanhtoan.as_view(),name='thanhtoan'),
    path('giohang/',views.giohang.as_view(),name='giohang'),
    path('tintuc/',views.tintuc.as_view(),name='tintuc' ),
    path('remove-from-cart/<id>/', views.remove_from_cart, name='remove-from-cart'),
    path('dangki/', views.dangki.as_view(), name='dangki'),
    path('dangnhap/', views.dangnhap.as_view(), name='dangnhap'),
    path('dangxuat/', views.logoutUser, name='dangxuat'),
    path('update-cart/<id>/', views.update_cart, name='update-from-cart'),
    path('donhang/', views.donhang.as_view(), name='donhang'),
    path('phanhoi/', views.phanhoi.as_view(), name='phanhoi'),
    path('label/<int:id>', XemTheoNganh.as_view(), name='label'),
    path('category/<int:id>', XemTheoLoai.as_view(), name='category'),
    path('xemchitiet/<int:news_id>/', views.ChiTietTinTuc, name='chitiettin'),
    path('search/', views.search, name='search'),


]
