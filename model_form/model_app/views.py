from django.shortcuts import render
from model_app.form import NewUserForm

# Create your views here.

def index(request):
    return render(request,'model_app/index.html')


def user(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR!")
    return render(request,'model_app/user.html',{'form' : form})