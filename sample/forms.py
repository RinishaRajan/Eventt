from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

	
	
class UserRegistrationForm(UserCreationForm):
	first_name = forms.CharField(max_length=101)
	last_name = forms.CharField(max_length=101)
	email = forms.EmailField()
	mobile = forms.IntegerField()
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email','mobile', 'password1', 'password2']




