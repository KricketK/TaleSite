from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def arena(request):
    return HttpResponse("Are you ready for combat?")
