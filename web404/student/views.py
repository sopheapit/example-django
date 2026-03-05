# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Staff
# Create your views here.

def home(request):
    return render(request,template_name='home.html')
def contact(request):
    return render(request,template_name='contact.html')
def about(request):
    return render(request,template_name='about.html')
def product(request):
    pro=Product.objects.all()
    return render(request,template_name='product.html',context={'p':pro})
def staff(request):
    st=Staff.objects.all()
    return render(request,template_name='staff.html',context={'staff_list':st})
def stafflist(request):
    st=Staff.objects.all()
    return render(request,template_name='stafflist.html',context={'staff_list':st})
def detail(request,id):
    dt=Staff.objects.get(id=id)
    return render(request,template_name='detail.html',context={'dt':dt})
