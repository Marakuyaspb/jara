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



# WANT THIS CAR
def handle_want_this_form(request):