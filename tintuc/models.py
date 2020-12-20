from django.db import models
from quanly.models import quanly
# Create your models here.
class tintuc(models.Model):
    tieude=models.CharField(default='',max_length=255)
    noidung=models.CharField(default='',max_length=255)
    ngaydang=models.DateTimeField(null=True)
    trangthai=models.BooleanField(default=True)
