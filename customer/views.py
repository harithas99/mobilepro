from django.shortcuts import render,redirect
from owner.models import Mobiles
from django.views.generic import View
from customer.forms import UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class CustomerIndex(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        return render(request,"custhome.html",{"mobiles":qs})

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,'signup.html',{'form':form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request,'signup.html',{'form':form})
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'signin.html',{'form':form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                print("login success")
                login(request,user)
                return redirect('custhome')
            else:
                print("login failed")
                return redirect(request,'signin.html',{'form':form})

def signout(request):
    logout(request)
    return redirect('signin')


