from django import forms
from django.contrib.auth.models import User
from .models import Queue_Entry

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password', 'email', 'first_name', 'last_name')

class UserLogin(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')

class QueueForm(forms.ModelForm):
	class Meta:
		model = Queue_Entry
		fields = ('machine',)