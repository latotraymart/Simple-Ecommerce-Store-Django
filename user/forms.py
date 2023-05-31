from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):

	First_name = forms.CharField(max_length=100)
	Last_name = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ('username', 'First_name', 'Last_name' ,'password1', 'password2')
