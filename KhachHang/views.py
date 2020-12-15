from django.shortcuts import render


from django.shortcuts import render,HttpResponse
from django.views import View


class Trangchu(View):
    def get(self,request):
        return render(request,'static/Quan_Ly/hangHoa.html')