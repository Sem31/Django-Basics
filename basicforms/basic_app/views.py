from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'basic_app/home.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #do something code
            print("validation success!")
            print('Name : ',form.cleaned_data['name'])
            print('Email : ',form.cleaned_data['email'])
            print('Text : ',form.cleaned_data['text'])
    return render(request,'basic_app/form.html',{'form':form})