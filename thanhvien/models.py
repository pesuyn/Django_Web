from django.db import models
from django import forms

# Create your models here.
class thanhvien(models.Model):
    choice = ((0, 'Nữ'), (1, 'Nam'))
    tendangnhap=models.CharField(max_length=255,null=True)
    matkhau=models.CharField(max_length=255,null=True)
    hovaten=models.CharField(max_length=255)
    sodienthoai=models.CharField(max_length=11,null=True)
    diachi=models.CharField(max_length=255,default='')
    avatar = models.ImageField(upload_to='')
    gioitinh=models.IntegerField(choices=choice,default=0)
    ngaydangky=models.DateTimeField(auto_now_add=True,null=True)
    ngaysinh=models.DateTimeField(null=True)
    trangthai = models.BooleanField(default=True)