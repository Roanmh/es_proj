from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

from .models import Consumer, Property, Installer, Quote


def index(request):
    return HttpResponse("Hello, world. You're at the picosage index.")


def properties_all(request):
    property_list = Property.objects.order_by('-date_posted')
    context = {
        'property_list': property_list,
    }
    return render(request, 'picosage/properties.html', context)


def property_single(request, property_id):
    _property = Property.objects.get(id=property_id)
    quote_list = Quote.objects.filter(property=_property.id)
    context = {
        'property': _property,
        'quote_list': quote_list
    }
    return render(request, 'picosage/property_details.html', context)
