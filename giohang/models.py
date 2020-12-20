from django.db import models
from sanpham.models import sanpham
from thanhvien.models import thanhvien
# Create your models here.
class giohang(models.Model):
    masanpham=models.ForeignKey("sanpham.sanpham",on_delete=models.CASCADE)
    thanhvien=models.ForeignKey("thanhvien.thanhvien",on_delete=models.CASCADE)
    soluong=models.IntegerField(default=0)
    ngaydatmua=models.DateTimeField(auto_now_add=True)
class giaodich(models.Model):
    giohang=models.ForeignKey("giohang.giohang",on_delete=models.CASCADE)
    sanpham=models.ForeignKey("sanpham.sanpham",on_delete=models.CASCADE)
    soluong=models.IntegerField(default=0)
    dongia=models.FloatField(default=0)
    ngaygiaodich=models.DateTimeField(auto_now=True)