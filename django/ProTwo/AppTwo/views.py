from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("My Second App")


def help(request):
    helpdict = {'help_insert': 'Help Page ho ne'}
    return render(request, 'apptwo/help.html', context=helpdict)
