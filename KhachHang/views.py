from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render,HttpResponse
from django.views import View
from KhachHang.models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone



class Trangchu(View):


    def get(self,request):
        context = {
            'items': product.objects.all(),
            'labels': label.objects.all(),
        }
        return render(request, 'static/Khach_Hang/TrangChu.html', context)


    # def viewProduct(self, request):
    #     context = {'items', product.objects.all()}
    #     return render(request, 'ChiTietSanPham.html')
#
class ChiTietSP(DetailView):
    model = product
    template_name = "static/Khach_Hang/ChiTietSanPham.html"
#     def get(self, request, product_id):
#         p = product.objects.get(pk=product_id)
#         context = {'item':p}
#         return render(request, 'static/Khach_Hang/ChiTietSanPham.html', context)


class thanhtoan(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/ThanhToan.html')
class tintuc(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/TinTuc.html')
class giohang(View):

    def get(self,request):
        return render(request,'static/Khach_Hang/GioHang.html')

class dangnhap(View):
    def get(self, request):
        return render(request, 'static/Khach_Hang/DangNhap.html')


def add_to_cart(request, slug):
    item = get_object_or_404(product, slug=slug)
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item_slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
    else:
        order_date = timezone.now()
        order = Order.objects.create(user=request.user, order_date = order_date)
        order.items.add(order_item)
    return redirect("KhachHang:product", slug=slug )