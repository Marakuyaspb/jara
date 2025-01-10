import os
import logging
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.template import loader

from .forms import *
from .models import *



# JUST CALL ME / phone + name /
def handle_callme_form(request):
	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		callme_form = CallMeForm(request.POST)

		if callme_form.is_valid():
			name = callme_form.cleaned_data['name']
			phone = callme_form.cleaned_data['phone']

			subject = f"Заявка на звонок от {name} с сайта SPB-JARA.NET"
			body = f"Имя: {name}\nТелефон: {phone}"


			send_mail(
				subject,
				body,
				'your_email@gmail.com',  # From email address
				['recipient@example.com'],  # To email address
				fail_silently=False,
			)



# WANT THIS
def handle_want_this_form(request):
	if request.method == 'POST':
		the_model = request.POST.get('the_model')
		want_this_form = WantThisForm(request.POST)

		if want_this_form.is_valid(): 
			want_this = want_this_form.save(commit=False)
			want_this.the_model = the_model
			want_this.save()

			name = want_this_form.cleaned_data['name']
			phone = want_this_form.cleaned_data['phone']

			subject = f"Заявка на звонок от {name} с сайта SPB-JARA.NET"
			body = f"Имя: {name}\n\nТелефон: {phone}\n\nЗаинтересовала модель: {the_model}"


			send_mail(
				subject,
				body,
				'your_email@gmail.com',  # From email address
				['recipient@example.com'],  # To email address
				fail_silently=False,
			)



def handle_fix_it_form(request):
	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		fix_it_form = FixItForm(request.POST)

		if fix_it_form.is_valid():
			name = fix_it_form.cleaned_data['name']
			phone = fix_it_form.cleaned_data['phone']
			problem = fix_it_form.cleaned_data['problem']

			subject = f"Заявка на звонок от {name} с сайта SPB-JARA.NET"
			body = f"Имя: {name}\n\nТелефон: {phone}\n\nОписание неполадок: {problem}"


			send_mail(
				subject,
				body,
				'your_email@gmail.com',  # From email address
				['recipient@example.com'],  # To email address
				fail_silently=False,
			)