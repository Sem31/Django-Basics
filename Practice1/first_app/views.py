from django.shortcuts import render
from first_app.models import AccessRecords,Webpages,Topic
from . import forms

# Create your views here.

def index(request):
    web_Data = AccessRecords.objects.order_by('date')
    return render(request,'first_app/index.html',{'data' : web_Data})

def form(request):
    form = forms.FormName()
    return render(request,'first_app/form.html',{'form':form})