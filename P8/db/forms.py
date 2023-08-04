from django.forms import ModelForm
from .models import User

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        exclude = ('firstname',)