from django import forms
from django.forms import ModelForm,PasswordInput
from models import *
		
class master_adminForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = master_admin
		fields = '__all__'