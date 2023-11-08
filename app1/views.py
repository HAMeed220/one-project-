from django.shortcuts import render

from django .http import HttpResponse

# Create your views here.

def affrin (request):
    return HttpResponse("<h1><marquee>'hi how are you akka '<marquee><h1>")
 


