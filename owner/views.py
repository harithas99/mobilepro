from django.shortcuts import render,redirect
from owner.forms import MobileForm
from django.views.generic import View
from owner.models import Mobiles
# Create your views here.

class AddMobile(View):
    def get(self,request):
        form=MobileForm()
        return render(request,"add_phone.html",{"form":form})
    def post(self,request):
        form=MobileForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # # print(form.cleaned_data)
            # print(form.cleaned_data.get("mobile_name"))
            # print(form.cleaned_data.get("colour"))
            # print(form.cleaned_data.get("battery"))
            # print(form.cleaned_data.get("storage"))
            # print(form.cleaned_data.get("ram"))
            # print(form.cleaned_data.get("processor"))
            # print(form.cleaned_data.get("weight"))
            # print(form.cleaned_data.get("price"))
            # qs=Mobiles(mobile_name=form.cleaned_data.get("mobile_name"),
            #            colour=form.cleaned_data.get("colour"),battery=form.cleaned_data.get("battery"),
            #            storage=form.cleaned_data.get("storage"),ram=form.cleaned_data.get("processor"),
            #            processor=form.cleaned_data.get("processor"),weight=form.cleaned_data.get("weight"),
            #            price=form.cleaned_data.get("price"))
            # qs.save()
            return redirect("allmobiles")

            # return render(request,"add_phone.html")
        else:
            return render(request,"add_phone.html",{"form":form})

class MobileListView(View):
    def get(self,request):
        qs=Mobiles.objects.all()
        return render(request,'mobile_list.html',{'mobiles':qs})

class MobileDetailView(View):
    def get(self,request,*args,**kwargs):
       # pass
       # kwargs={'id':3}
        qs=Mobiles.objects.get(id=kwargs.get("id"))
        return render(request,'mobile_detail.html',{'mobile':qs})

class MobileDeleteView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allmobiles")

class ChangeMobile(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.get(id=kwargs.get("id"))
        form=MobileForm(instance=qs)
        return render(request,"mobile_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        qs=Mobiles.objects.get(id=kwargs.get("id"))
        form=MobileForm(request.POST,instance=qs)
        if form.is_valid():
            form.save()
            print("book created")
            return redirect("allmobiles")

