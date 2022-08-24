from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


# Create your views here.




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)


        if user is not None:
            auth.login(request, user)
            return render(request,'forms.html')
        else:
            messages.info(request,"invalid login try again")
            return redirect('login')

    return render(request,'login.html')

def register(request):
        if request.method == 'POST':
              username=request.POST['username']
              password = request.POST['password']
              cpassword = request.POST['password1']
              if password==cpassword:
                  if User.objects.filter(username=username).exists():
                      messages.info(request,"user name taken")
                      return render(request,'register.html')
                  else:
                       user=User.objects.create_user(username=username,password=password)
                       user.save();
                       return render(request,'login.html')




              else:
                  messages.info(request,"invalid login ty again")
                  return redirect('register')

        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
