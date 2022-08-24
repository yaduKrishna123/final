from django.contrib import messages
from django.shortcuts import render, redirect
from .models import bank
# Create your views here.


def forms(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        DOB = request.POST.get('DOB', )
        AGE = request.POST.get('AGE', )
        phone = request.POST.get('phone', )
        mail = request.POST.get('mail',)
        adress = request.POST.get('adress', )
        district = request.POST.get('district', )
        branch = request.POST.get('branch', )
        account = request.POST.get('account', )
        materials = request.POST.get('materials', )
        Bank=bank(name=name,DOB=DOB,AGE=AGE,phone=phone,mail=mail,adress=adress,district=district,branch=branch,account=account,materials=materials)
        Bank.save()
        messages.info(request,"Application Accepted")


    return render(request,'forms.html')

def demo(request):
    return render(request,'home.html')
def login(request):
   return render(request, 'login.html')


