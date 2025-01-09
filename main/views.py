import os
from django.shortcuts import render
from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template, render_to_string
from django.urls import reverse

from cars.models import *
from cars.forms import *
from cars.forms_generator import *
from cars.tasks import * 


def custom_404_view(request, exception):
    return render(request, 'main/404.html', status=404)
    
def custom_500_view(request):
    return render(request, 'main/500.html', status=500)


def index(request):
	cars = Car.objects.all()
	new_cars = Car.objects.filter(status=1)
	used_cars = Car.objects.filter(status=2)

	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
		'cars' : cars,
		'new_cars': new_cars,
		'used_cars': used_cars,
	}
	return render(request, 'main/index.html', context)



def contact(request):
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/contact.html', context)

	

def feedback(request):
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/feedback.html', context)

	

def install(request):
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/install.html', context)



def portfolio(request):
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/portfolio.html', context)
	


def service(request):
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/service.html', context)
	


def stock(request):
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/stock.html', context)
	


def ventilation(request):
	callme_form = handle_callme_form(request)

	context = {
		'callme_form': callme_form,
	}
	return render(request, 'main/ventilation.html', context)