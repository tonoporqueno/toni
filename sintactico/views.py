from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def sintac(request):
    template_name = 'sintactico/sintactico.html'
    return render(request, template_name)
