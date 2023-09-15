from django import forms
from .models import User, Bookmark

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('firstname',)


