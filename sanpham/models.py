from django.db import models
# Create your models here.
class loaihang(models.Model):
    tenloaihang=models.CharField(default='',max_length=255)
    trangthai=models.BooleanField(default=True)
    nganhhanh=models.ForeignKey("nganhhanh",on_delete=models.CASCADE)
class nganhhanh(models.Model):
    tennganhhang=models.CharField(default='',max_length=255)
    trangthai=models.BooleanField(default=True)

class sanpham(models.Model):
    tensanpham=models.CharField(default='',max_length=255)
    giatien=models.FloatField(default=0.0)
    ngaynhap=models.DateTimeField
    soluong=models.IntegerField(default=0)
    anh = models.ImageField(upload_to='')
    mota=models.CharField(default='',max_length=500)
    trangthai=models.BooleanField(default=True)
    loaihang=models.ForeignKey("loaihang",on_delete=models.CASCADE,null=True)
    nhacungcap=models.ForeignKey("nhacungcap",on_delete=models.CASCADE,null=True)
class nhacungcap(models.Model):
    tennhacungcap=models.CharField(default='',max_length=255)
    diachinhacungcap=models.CharField(default='',max_length=255)
    dienthoainhacungcap=models.IntegerField
    trangthai=models.BooleanField(default=True)
