from django.shortcuts import render
from user_app.models import User,AccessRecord

# Create your views here.

def index(request) :
    return render(request,'index.html',context = None)


def index1(request) :
    record_list  = User.objects.order_by('Name')
    record_dict  = {'AccessRecord' : record_list}
    return render(request,'user.html',context = record_dict)