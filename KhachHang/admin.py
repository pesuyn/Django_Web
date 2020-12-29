from django.contrib import admin
from KhachHang.models import product,bill,news,report,category,supplier,Profile,cart,label,Order, OrderItem
# Register your models here.
admin.site.register(product)
admin.site.register(bill)
admin.site.register(news)
admin.site.register(report)
admin.site.register(category)
admin.site.register(Profile)
admin.site.register(cart)
admin.site.register(label)
admin.site.register(supplier)
admin.site.register(OrderItem)
admin.site.register(Order)



