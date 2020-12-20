from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,UserManager
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User
from django.contrib import admin
# Create your models here.
class quanly(admin.ModelAdmin):
    choice = ((0, 'Nữ'), (1, 'Nam'))
    choice1 = ((0, 'Admin'), (1, 'Nhân viên'))
    sodienthoai=models.IntegerField(default=0)
    gioitinh=models.IntegerField(choices=choice,default=0)
    loai=models.IntegerField(choices=choice1,default=0)

