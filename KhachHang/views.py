from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import View


class Trangchu(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/TrangChu.html')
class thanhtoan(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/ThanhToan.html')
class tintuc(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/TinTuc.html')
class giohang(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/GioHang.html')