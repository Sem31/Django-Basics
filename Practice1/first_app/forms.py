from django import forms

class FormName(forms.Form):
    name = forms.CharField(max_length=45, required=False)
    email = forms.EmailField(required=False)