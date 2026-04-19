# views.py
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product,Staff,Contactus
from .form import Contactform,Staffform
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
def contactus(request):
    fr=Contactform()
    if(request.method=='POST'):
        form_data=Contactform(request.POST)
        if(form_data.is_valid()):
            full_name=form_data.cleaned_data['full_name']
            phone=form_data.cleaned_data['phone']
            email=form_data.cleaned_data['email']
            detail=form_data.cleaned_data['detail']
            new_contact=Contactus.objects.create(
                full_name=full_name,
                phone=phone,
                email=email,
                detail=detail
            )
            new_contact.save()
            return redirect('home')
            return HttpResponse("Thanks you")
    else:
        return render(request,template_name='contactus.html',context={'form_contact':fr})
def delete(request,id):
    st=Staff.objects.get(id=id)
    if(st!=''):
        st.delete()
        return redirect('staff')
def update(request,id):
    st=Staff.objects.get(id=id)
    init_data={
        'full_name':st.full_name,
        'phone':st.phone,
        'email':st.email,
        'gender':st.gender,
        'address':st.address,
        'photo':st.photo
    }
    frm=Staffform(initial=init_data)
    if(request.method=='POST'):
        data_form=Staffform(request.POST,request.FILES)
        if data_form.is_valid():
            st.full_name=data_form.cleaned_data['full_name']
            st.phone=data_form.cleaned_data['phone']
            st.email=data_form.cleaned_data['email']
            st.gender=data_form.cleaned_data['gender']
            st.address=data_form.cleaned_data['address']
            st.save()
            return redirect('staff')
    else:
        return render(request,template_name='update.html',context={'frm':frm})




