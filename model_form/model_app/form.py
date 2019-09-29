from django import forms
from model_app.models import  User1

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User1
        fields = '__all__'

