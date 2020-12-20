from django.contrib import admin
from thanhvien.models import thanhvien
from sanpham.models import sanpham,loaihang,nhacungcap,nganhhanh
from tintuc.models import tintuc
from phanhoi.models import phanhoi
from django.contrib.auth.admin import UserAdmin



# Register your models here.

admin.site.register(thanhvien)
admin.site.register(loaihang)
admin.site.register(nhacungcap)
admin.site.register(sanpham)
admin.site.register(nganhhanh)
admin.site.register(tintuc)
admin.site.register(phanhoi)
