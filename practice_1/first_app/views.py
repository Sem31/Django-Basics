from django.shortcuts import render

# Create your views here.

def index(request):
    dict = {'data' : "form the dictionary "}
    return render(request,'first.html',context = dict)