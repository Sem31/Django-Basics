from django.shortcuts import render

# Create your views here.

def index(request) :
    dict = { 'insert_me' : 'this is form the views.py to use by the expression tag',
            'insert_two' : 5,
            }
    return render(request,'first_app/index.html', context= dict)