from django.db.models import Count, Q
from .models import *



def products_ordering(instance, queryset, sort_by):
	if sort_by == 'asc':
		return queryset.order_by('price')
	elif sort_by == 'desc':
		return queryset.order_by('-price')
	else:
		return queryset