from django.shortcuts import render
from django.http import HttpResponse
from .models import Phonesmode

def index(request):
    phones = Phonesmodes.objects.all()
    return render (request, "index.html",{ 'phones': phones})


def new(request):
    return HttpResponse("Available phones")
