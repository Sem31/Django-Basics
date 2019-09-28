from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request) :
    return HttpResponse("Hello sem form first app !")

def new_index(request) :
    return HttpResponse("Hello sem!")