from django import forms
from .models import Upload

from django.contrib.auth.models import User
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ('username','password','email','first_name','last_name')
        widgets={'password':forms.PasswordInput()}


class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload
        fields=('name','pic')