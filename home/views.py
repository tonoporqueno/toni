from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from home.models import tessio
# Create your views here


def micasa(request):
    Lista = tessio.objects.get_queryset()
    template_name = 'home/index.html'
    # diccionariodecontexto = {'lista': {1, 2, 3, 4, 5, 6}}
    return render(request, template_name, {'l': Lista})
