from django import forms
from .models import *


class CallMeForm(forms.ModelForm):
	class Meta:
		model = CallMe
		fields = ['first_name', 'phone']
		labels = {
		'first_name': 'Имя',
		'phone': 'Телефон',
		}


class WantThisForm(forms.ModelForm):
	class Meta:
		model = WantThisCar
		fields = ['first_name', 'phone', 'the_model']
		labels = {
		'first_name': 'Имя',
		'phone': 'Телефон'
		}
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['the_model'].required = False