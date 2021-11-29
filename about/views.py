from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here


def about(request):
    resultado = mifuncion(request)
    template_name = 'about/about.html'
    return render(request, template_name, {"nombreusuario": resultado, 'edad': 45})


def mifuncion(args):
    return 'tono'


# def about(request):
#     return render(request, '\about.html')
