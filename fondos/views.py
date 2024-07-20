from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hola estamos en el index de la App 'FONDOS'")