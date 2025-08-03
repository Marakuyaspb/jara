import os
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, F, Count, Value
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template

from .models import *
from .forms import *
from .filters import *


def catalog(request):
	sort_by = request.GET.get('sort_by', 'asc')
	products = Product.objects.all()
	products = products_ordering(Product, products, sort_by)


	callme_form = CallMeForm()

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
	
		
	context = {'callme_form': callme_form}

	return render(request, 'catalog/catalog.html', context)


def the_product(request, id):
	if id:
		the_car = get_object_or_404(Product, id=id)

		callme_form = CallMeForm()
		want_this_form = WantThisForm()

		want_this = None

	if request.method == 'POST':
		form_type = request.POST.get('form_type')
		if form_type == 'call_me':
			callme_form = handle_callme_form(request)
		elif form_type == 'want_this_car':
			want_this_car = handle_want_this_form(request)
			print(want_this_form.errors) 

	context = {
		'callme_form': callme_form,
		'want_this_form': want_this_form,
	}

	return render(request, 'catalog/catalog.html', {'callme_form': callme_form})
