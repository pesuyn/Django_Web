from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class cart(models.Model):
    name = models.CharField(default='', max_length=255)
    price=models.FloatField(default=0.0)
    quantity=models.IntegerField(default=0)
    totalprice = models.FloatField(default=0)
    create_dau=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class bill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cart = models.ForeignKey("cart",on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    totalprice=models.FloatField(default=0)
    def __str__(self):
        return self.user
class report(models.Model):
    choice = ((0, 'Khiếu nại'), (1, 'Báo cáo'),(2, 'Đánh giá'))
    choice1 = ((0, 'Đã xem'), (1, 'Chưa xem'),(2,'Đã phản hồi'))
    type=models.IntegerField(choices=choice,default=0)
    title=models.CharField(default='',max_length=255)
    reporter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    content =models.CharField(default='',max_length=255)
    create_day=models.DateTimeField(null=True)
    status=models.IntegerField(choices=choice1,default=1)
    def __str__(self):
        return self.title

class category(models.Model):
    name=models.CharField(default='',max_length=255)
    status=models.BooleanField(default=True)
    label=models.ForeignKey("label",on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class label(models.Model):
    name=models.CharField(default='',max_length=255)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class product(models.Model):
    name=models.CharField(default='',max_length=255)
    price=models.FloatField(default=0.0)
    create_day=models.DateTimeField
    quantity=models.IntegerField(default=0)
    image = models.ImageField(upload_to='')
    description=models.CharField(default='',max_length=500)
    status=models.BooleanField(default=True)
    category=models.ForeignKey("category",on_delete=models.CASCADE,null=True)
    supplier=models.ForeignKey("supplier",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
class supplier(models.Model):
    name=models.CharField(default='',max_length=255)
    address=models.CharField(default='',max_length=255)
    phone=models.IntegerField
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.supplier_name
class news(models.Model):
    title=models.CharField(default='',max_length=255)
    content=models.CharField(default='',max_length=255)
    create_day=models.DateTimeField(null=True)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile',null=True)
    choice = ((0, 'Nữ'), (1, 'Nam'))
    username = models.CharField(max_length=255,null=True)
    phone=models.CharField(max_length=11,null=True)
    address=models.CharField(max_length=255,default='',null=True)
    avatar = models.ImageField(upload_to='')
    sex=models.IntegerField(choices=choice,default=0,null=True)
    create_day=models.DateTimeField(auto_now_add=True,null=True)
    date=models.DateTimeField(null=True,)
    status = models.BooleanField(default=True,null=True)



    def __str__(self):
        return self.username