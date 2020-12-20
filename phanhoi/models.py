from django.db import models
from thanhvien.models import thanhvien
# Create your models here.
class phanhoi(models.Model):
    choice = ((0, 'Khiếu nại'), (1, 'Báo cáo'),(2, 'Đánh giá'))
    choice1 = ((0, 'Đã xem'), (1, 'Chưa xem'),(2,'Đã phản hồi'))
    loaiphanhoi=models.IntegerField(choices=choice,default=0)
    tieude=models.CharField(default='',max_length=255)
    nguoiphanhoi=models.ForeignKey("thanhvien.thanhvien",on_delete=models.CASCADE,null=True)
    noidung=models.CharField(default='',max_length=255)
    ngaygui=models.DateTimeField(null=True)
    trangthai=models.IntegerField(choices=choice1,default=1)