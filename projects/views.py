from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    msg = "Hello, you are on the projects page"
    number = 3
    context = {"message": msg, "number": number}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    #return HttpResponse(f'Aquí es mostrarà un projecte: {str(pk)}')    
    return render(request, 'projects/single-project.html')

 