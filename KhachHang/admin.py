from django.contrib import admin
<<<<<<< HEAD
from KhachHang.models import product,bill,news,report,category,supplier,Profile,label,Order, OrderItem
=======
from KhachHang.models import product,bill,news,report,category,supplier,Profile,cart,label
>>>>>>> refs/remotes/origin/main
# Register your models here.
admin.site.register(product)
admin.site.register(bill)
admin.site.register(news)
admin.site.register(report)
admin.site.register(category)
admin.site.register(Profile)
admin.site.register(label)


