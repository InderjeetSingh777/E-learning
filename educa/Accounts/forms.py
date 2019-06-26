from django import forms
from .models import User 
from django.contrib.auth.forms import UserCreationForm
from django.db import models
class RegistrationForm(UserCreationForm):
	full_name=forms.CharField(required= True)
	class Meta:
		model=User 
		fields=('username','full_name','password1','password2')

		def save(self,commit=True):
			user=super(RegistrationForm,self).save(commit=False)
			user.full_name=cleaned_data['full_name']

			if commit:
				user.save()
			return user
			