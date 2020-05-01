from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from .models import Profile
from django.forms.widgets import SelectDateWidget
from blog_project import settings

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username','email','password1','password2')
		labels = {'username':'Kullanıcı Adı'}
		

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','first_name','last_name']
		

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image','bio','location','birth_date']
		error_messages = {'birth_date':{'invalid':'Lütfen tarih değeri girin'}}

