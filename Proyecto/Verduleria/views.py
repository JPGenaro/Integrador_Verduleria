from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bienvenida(request):
    return HttpResponse("Bienvenido a Mercado Fenix")