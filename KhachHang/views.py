
from django.shortcuts import render
from django.views import View
from django.contrib import messages

from .models import Profile
from templates import static
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required



login_required(login_url='dangnhap')
class Trangchu(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/TrangChu.html')

class dangki(View):
    def get(self, request):
        return render(request, 'static/Khach_Hang/register.html')

    def post(self, request):
        # f = CreateUserForm()
        if request.method == 'POST':
            hovaten = request.POST['hovaten']
            name = request.POST['tendangnhap']
            pw = request.POST['matkhau']
            pw1 = request.POST['nhaplaimatkhau']
            phone = request.POST['sodienthoai']
            email = request.POST['email']
            avatar = request.POST['avatar']
            gioitinh = request.POST.get('gioitinh', False)
            diachi = request.POST['diachi']
            alluser=User.objects.all()
            dem=0



            for i in alluser:
                if i.get_username() == name or i.get_email_field_name() == email:
                    dem=1
            if dem==1:
                messages.info(request, "Tên đăng nhập hoặc email đã tồn tại")
                return render(request, 'static/Khach_Hang/register.html')
            else:
                if (pw1 == pw and name!=pw and name!= pw1 ) :
                    for i in Profile.objects.all():
                        if i.phone == phone:
                            messages.info(request, "Số điện thoại đã tồn tại")
                            return render(request, 'static/Khach_Hang/register.html')
                        else:
                            user = User.objects.create_user(username=name, password=pw, email=email)
                            user.save()

                            user1 = User.objects.get(username=name)
                            profile = Profile.objects.create(user=user1,username=hovaten,avatar=avatar,sex=gioitinh,address=diachi, phone=phone )
                            profile.save()
                            my_group = Group.objects.get(name='Users')
                            my_group.user_set.add(user1)
                            messages.info(request, "Đăng kí thành công, hãy đăng nhập")
                            return render(request, 'static/Khach_Hang/login.html')
                else:
                    messages.info(request, "Đăng kí thất bại, vui lòng nhập lại")
                    return render(request, 'static/Khach_Hang/register.html')

class dangnhap(View):
    def get(self, request):

        return render(request, 'static/Khach_Hang/login.html')

    def post(self, request):
        username = request.POST.get('tendangnhap')
        password = request.POST.get('matkhau')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'static/Khach_Hang/TrangChu.html')
        else:
            messages.error(request, "Đăng nhập thất bại, nhập lại tài khoản")
            return render(request, 'static/Khach_Hang/login.html')

def logoutUser(request):
    logout(request)
    return render(request, 'static/Khach_Hang/TrangChu.html')






class thanhtoan(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/ThanhToan.html')
class tintuc(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/TinTuc.html')
class giohang(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/GioHang.html')

class chitietsanpham(View):
    def get(self,request):
        return render(request,'static/Khach_Hang/ChiTietSanPham.html')