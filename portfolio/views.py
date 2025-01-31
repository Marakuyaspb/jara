import os
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F, Count, Value
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from .models import *


def portfolio(request):
	cases = Case.objects.all()

	callme_form = CallMeForm()

		if request.method == 'POST':
			form_type = request.POST.get('form_type')
			if form_type == 'call_me':
				callme_form = handle_callme_form(request)
		
			
		context = {'callme_form': callme_form}

		return render(request, 'portfolio.html', context)


def the_case(request, id):
	if id:
		the_car = get_object_or_404(Case, id=id)

		callme_form = CallMeForm()

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
 
	context = {
		'callme_form': callme_form,
	}

	return render(request, 'the_case.html', {'callme_form': callme_form})
