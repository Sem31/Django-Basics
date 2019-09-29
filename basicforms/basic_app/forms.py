from django import forms
from django.core import validators

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name Need to start with Z ')

class FormName(forms.Form):
    # name = forms.CharField(max_length=50, required=False,validators=[check_for_z])
    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    verify_Email = forms.EmailField(label="Enter teh email Again",required=False)
    text = forms.CharField(max_length=50, required=False, widget = forms.Textarea)
    botcatcher = forms.CharField(max_length=40, required=False,
                                widget = forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_Email']

        if email != vmail:
            raise forms.ValidationError('Make sure your email is matched')



