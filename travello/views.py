from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def home(request):
    Destinations = Destination.objects.all()
    return render(request, 'index.html', {'Destinations' : Destinations})

def about(request):
    return HttpResponse("This is about page of travello")
