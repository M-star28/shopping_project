from django.shortcuts import render
from django.http import HttpResponse
from .models import Fruits
from django.template import loader


def fruits(request):
    af = Fruits.objects.all()
    template = loader.get_template('shopping_app/Fruits.html')
    context = {
        'af': af,
    }
    return HttpResponse(template.render(context, request))

