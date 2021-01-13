from urllib import request

from django.contrib import messages
from django.core.mail import send_mail

from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render,HttpResponse
from django.views import View
from KhachHang.models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone

from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import Profile
from templates import static
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
import random
from Django_Web import settings
from django.core.mail import EmailMultiAlternatives


login_required(login_url='dangnhap')


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
            gioitinh = request.POST['gioitinh']
            diachi = request.POST['diachi']
            alluser=User.objects.all()
            dem=0

            for i in Profile.objects.all():
                if i.phone == phone :
                    messages.info(request, "Số điện thoại đã tồn tại")
                    return render(request, 'static/Khach_Hang/register.html')

            for i in alluser:
                if i.get_username() == name or i.get_email_field_name() == email:
                    dem=1
            if dem==1:
                messages.info(request, "Tên đăng nhập hoặc email đã tồn tại")
                return render(request, 'static/Khach_Hang/register.html')
            else:
                if (pw1 == pw and name!=pw and name!= pw1 ) :
                    user = User.objects.create_user(username=name, password=pw, email=email)
                    user.last_name=hovaten
                    user.save()
                    user1 = User.objects.get(username=name)
                    profile = Profile.objects.create(user=user1,username=hovaten,avatar=avatar,sex=gioitinh,address=diachi, phone=phone )
                    profile.save()
                    my_group = Group.objects.get(name='Users')
                    my_group.user_set.add(user1)
                    content = '<h1> <strong>Cảm ơn bạn đã đăng ký tài khoản</strong></h1> ' + '<p><strong>Tài khoản:</strong> </p>' + name + '<p><strong>Mật khẩu:</strong> </p>' + pw
                    mail=str(email)
                    subject, from_email, to = 'Đăng ký tài khoản thành công', 'shoppingonlinedjango@gmail.com', mail
                    text_content = 'Đăng ký tài khoản'

                    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                    msg.attach_alternative(content, "text/html")
                    msg.send()
                    return redirect('trang-chu:dangnhap')
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
            #return render(request, 'static/Khach_Hang/TrangChu.html')
            return redirect('trang-chu:trangchu')
        else:
            messages.error(request, "Đăng nhập thất bại, nhập lại đúng thông tin")
            return render(request, 'static/Khach_Hang/login.html')


def logoutUser(request):
    logout(request)
    return redirect('trang-chu:trangchu')



class Trangchu(View):



    def get(self,request):
        all_product = list(product.objects.all())
        recommend_product = random.sample(all_product, 3)
        recommend_product1 = random.sample(all_product, 3)
        labs = label.objects.all()
        cat=category.objects.all()
        context = {
            'items': product.objects.all(),
            'labels': labs,
            'random': recommend_product,
            'random1':recommend_product1,
            'cat':cat
        }
        return render(request, 'static/Khach_Hang/TrangChu.html', context)


    # def viewProduct(self, request):
    #     context = {'items', product.objects.all()}
    #     return render(request, 'ChiTietSanPham.html')
#
# class ChiTietSP(DetailView):
#     model = product
#     template_name = "static/Khach_Hang/ChiTietSanPham.html"
# #     def get(self, request, product_id):
# #         p = product.objects.get(pk=product_id)
# #         context = {'item':p}
# #         return render(request, 'static/Khach_Hang/ChiTietSanPham.html', context)
class ChiTietSP(DetailView):


    def get(self, request, id):
        item = product.objects.get(id=id)
        labs = label.objects.all()
        cat = category.objects.all()
        all_product = list(product.objects.all())
        recommend_product = random.sample(all_product, 3)
        recommend_product1 = random.sample(all_product, 3)
        context = {
            'products':item,
            'labs':labs,
            'cates':cat,
            'labels': label.objects.all(),
            'random': recommend_product,
            'random1': recommend_product1,

        }
        return render(request, "static/Khach_Hang/ChiTietSanPham.html", context)


class thanhtoan(View):
    def post(self, request):
        totalprice = request.POST['totalprice']
        quantity = request.POST['quantity']
        all=Order.objects.filter(user=request.user)
        max=0
        if all.exists():
            for item in all:
                if item.trade_time > max:
                    max=item.trade_time
        all1 = bill.objects.filter(user_id=request.user)
        maxx = 0
        content = '<h1> <strong>Cảm ơn bạn đã mua hàng</strong></h1> ' \
                  '<p> </p>' + '<strong> Sản phẩm đã mua</strong>' +    '<p> </p>'

        if all1.exists():
            for i in all1:
                if i.trade_time > maxx:
                    maxx = i.trade_time
        if Order.objects.filter(user=request.user,ordered=False).exists():
            bill.objects.create(user=request.user,Order=Order.objects.get(user=request.user,trade_time=max),totalprice=totalprice,quantity=quantity,trade_time=maxx+1).save()
            Ordered=Order.objects.get(user=request.user,trade_time=max)
            Ordered.ordered=True
            Ordered.save(update_fields=['ordered'])
            for item in  OrderItem.objects.filter(user=request.user):
                if item.ordered == False:
                    product1=product.objects.get(name=item.item.name)
                    if product1.quantity < item.quantity:
                        product1.quantity =0
                    else:
                        product1.quantity-=item.quantity
                    product1.save(update_fields=['quantity'])
                    nameitem=str(item.item.name)
                    br=str('<p> </p>')
                    space=str( ' : ')
                    quan=str(item.quantity)
                    content += nameitem +space+ quan+br
                item.ordered=True
                item.save(update_fields=['ordered'])
            user = User.objects.get(id=request.user.id)
            mail = str(user.email)
            subject, from_email, to = 'Đặt hàng thành công', 'shoppingonlinedjango@gmail.com', mail
            text_content = 'Đặt hàng'
            sum= ' <strong> Số lượng sản phẩm đã mua  </strong>' + quantity + '<p> </p>' + \
                  '<strong> Tổng số tiền </strong>' + totalprice
            content+=sum
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(content, "text/html")
            msg.send()
        return redirect("trang-chu:trangchu")

    def get(self, request):
        if request.user.is_anonymous:
            context = {
                'labels': label.objects.all(),
            }
            return render(request, 'static/Khach_Hang/ThanhToan.html',context)
        else:

            user=request.user
            list1 = []
            listprice = []
            listquantity = []
            total = 0
            quantity = 0
            allitem = OrderItem.objects.filter(
                user=request.user,
                ordered=False
            )
            if allitem.exists():
                for item in allitem:
                    listprice.append(item.item.price)
                    listquantity.append(item.quantity)
                    quantity += item.quantity
                    if item.user == request.user:
                        list1.append(item)
                for i in range(0, len(listquantity)):
                    total += listprice[i] * listquantity[i]
                contex = {'items': list1, 'object': product.objects.all(),  'labels': label.objects.all(),'quantity': quantity, 'total': total,"profile": Profile.objects.get(user=request.user)}
                return render(request, 'static/Khach_Hang/ThanhToan.html', contex)

            contex = {"profile": Profile.objects.get(user=request.user), 'labels': label.objects.all()}
            return render(request, 'static/Khach_Hang/ThanhToan.html',contex  )


class tintuc(View):

    def get(self,request):
        n = news.objects.all()
        return render(request,'static/Khach_Hang/TinTuc.html',{'news':n,'labels': label.objects.all()})


def ChiTietTinTuc(request, news_id):
    tintuc = news.objects.get(pk=news_id)
    return render(request,'static/Khach_Hang/ChiTietTinTuc.html', {'news':tintuc,'labels': label.objects.all()})

class giohang(View):

    def get(self,request):
        # allitem=OrderItem.objects.all()

        list1=[]
        listprice=[]
        listquantity=[]
        total=0
        quantity=0
        if request.user.is_anonymous:
            return render(request,'static/Khach_Hang/GioHang.html')
        else:
            allitem=OrderItem.objects.filter(
                user=request.user,
                ordered=False
            )

            if allitem.exists():
                for item in allitem:
                    listprice.append(item.item.price)
                    listquantity.append(item.quantity)
                    quantity+=item.quantity
                    if item.user==request.user:
                        list1.append(item)
                for i in range(0,len(listquantity)):
                    total+=listprice[i]*listquantity[i]
                contex={'items': list1,'object': product.objects.all(),'quantity':quantity, 'labels': label.objects.all(),'total':total}
                return render(request,'static/Khach_Hang/GioHang.html',contex)
            return render(request,'static/Khach_Hang/GioHang.html',{ 'labels': label.objects.all()})



def add_to_cart(request, id):
    all = Order.objects.filter(user=request.user)
    max = 0
    if all.exists():
        for item in all:
            if item.trade_time > max:
                max = item.trade_time
    all1 = OrderItem.objects.filter(user=request.user,ordered=True)
    max1 = 0
    if all1.exists():
        for item in all1:
            if item.trade_time > max1:
                max1 = item.trade_time

    item = get_object_or_404(product, id=id)
    order_item=OrderItem

    order_item,created = OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False,trade_time=max1+1)

    order_qs = Order.objects.filter(user=request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()

        else:

            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user,trade_time=max+1)
        order.items.add(order_item)

    return redirect("trang-chu:giohang")
def add_1(request, id):
    all = Order.objects.all()
    max = 0
    if all.exists():
        for item in all:
            if item.trade_time > max:
                max = item.trade_time
    item = get_object_or_404(product, id=id)
    order_item,created = OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False,)
    order_qs = Order.objects.filter(user=request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()

        else:

            order.items.add(order_item)
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user,trade_time=max+1)
        order.items.add(order_item)

    return redirect("trang-chu:giohang")



def remove_from_cart(request, id):
    item = get_object_or_404(product, id=id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()

            return redirect("trang-chu:giohang")
        else:

            return redirect("trang-chu:giohang")
    else:

        return redirect("trang-chu:giohang")
def update_cart(request, id):
    item = get_object_or_404(product, id=id)
    order_item = OrderItem.objects.filter(
        item=item,
        user=request.user,
        ordered=False
    )[0]
    order_item.quantity=order_item.quantity-1
    if order_item.quantity==0:
        order_item.delete()
    else:
        order_item.save(update_fields=['quantity'])

    return redirect("trang-chu:giohang")
class donhang(View):
    def get(self, request):
        all=bill.objects.filter(user=request.user)
        # all = Order.objects.all()
        # max = 0
        # if all.exists():
        #     for item in all:
        #         if item.trade_time > max:
        #             max = item.trade_time
        all1=all.order_by('date').reverse()
        order=Order.objects.filter(user=request.user)
        order_item=OrderItem.objects.filter(user=request.user)
        list1 = []
        for i in order:
            if OrderItem.objects.filter(user=request.user, trade_time=i.trade_time).exists():
                list1.append(OrderItem.objects.filter(user=request.user, trade_time=i.trade_time))
                print(OrderItem.objects.filter(user=request.user, trade_time=i.trade_time))

        contex={'all':all1,'list':list1, 'labels': label.objects.all()}
        return render(request, 'static/Khach_Hang/DonHang.html',contex)

class phanhoi(View):
    def get(self, request):

        return render(request, 'static/Khach_Hang/PhanHoi.html', {'labels':label.objects.all()})
    def post(self,request):
        title = request.POST['tieude']
        content = request.POST['noidung']
        type = request.POST['loai']
        report.objects.create(reporter=request.user,title=title,content=content,type=type)
        return render(request, 'static/Khach_Hang/TrangChu.html')

def search(request):
    cates = category.objects.all()
    if request.method == "GET":
        search = request.GET.get('search')
        post = product.objects.all().filter(name__icontains=search)

        return render(request, 'static/Khach_Hang/TimKiemHang.html', {'post':post,  'labels': label.objects.all(),'cates':cates})



class XemTheoNganh(ListView):
    def get(self, request, id):
        lab = label.objects.get(id=id)
        cate = category.objects.get(id=id)
        pro = product.objects.filter(label=lab)
        cate_all = category.objects.all()
        return render(request, 'static/Khach_Hang/XemTheoNganh.html', {'label':lab,'products':pro,  'labels': label.objects.all(),'cate':cate, 'cates':cate_all })


class XemTheoLoai(ListView):
    def get(self, request, id):
        cate = category.objects.get(id=id)
        pro = product.objects.filter(category=cate)
        return render(request, 'static/Khach_Hang/XemTheoLoai.html', {'cate':cate,  'labels': label.objects.all(),'products':pro,})

def search(request):
    cates = category.objects.all()
    if request.method == "GET":
        search = request.GET.get('search')
        post = product.objects.all().filter(name__icontains=search)

        return render(request, 'static/Khach_Hang/TimKiemHang.html', {'post':post, 'cates':cates})


