from django.shortcuts import render
from . import form
# Create your views here.

def index(request):
    return render(request,'index.html', context = None)

def formView(request) :
    forms = form.FromName()
    if request.method == "POST":
        forms = form.FromName(request.POST)
        if forms.is_valid():
            print("form is the valid")
            print("Name : "+forms.cleaned_data['Name'])
            print("email : "+forms.cleaned_data['email'])
            print("text : "+forms.cleaned_data['text'])
    return render(request,'form.html',context = {'form' : forms})