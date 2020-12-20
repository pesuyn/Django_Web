from django.db import models
from thanhvien.models import thanhvien
from giohang.models import giohang
# Create your models here.
class hoadon(models.Model):
    thanhvien=models.ForeignKey("thanhvien.thanhvien",on_delete=models.CASCADE)
    giohang = models.ForeignKey("giohang.giohang",on_delete=models.CASCADE)
    thanhtoan=models.IntegerField(default=0)
    thanhtien=models.FloatField(default=0)
