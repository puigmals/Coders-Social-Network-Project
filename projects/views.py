from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Aquí es mostraran tots els projectes')

def project(request, pk):
    return HttpResponse('Aquí es mostrara un projecte: {}'.format(str(pk)))    

