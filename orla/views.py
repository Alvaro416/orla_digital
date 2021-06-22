from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Curso
from .models import Orla


def orla_list(request):
    curso = Curso.objects.filter(num='1')
    orla = Orla.objects.filter(estado='profe')
    orla2 = Orla.objects.filter(estado='alumno')
    return render(request, 'orla.html', {'curso': curso, 'orla': orla, 'orla2': orla2})
