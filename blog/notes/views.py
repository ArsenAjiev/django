from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index2(request):
   return HttpResponse("Notes index2 view- Hello world-2")