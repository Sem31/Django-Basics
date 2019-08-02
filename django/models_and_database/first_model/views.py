from django.shortcuts import render
from django.http import HttpResponse
from first_model.models import AccessRecord,Topic,Webpage
# Create your views here.

def index(request) :
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'AccessRecords' : webpage_list}
    return render(request,'index.html', context = date_dict)
