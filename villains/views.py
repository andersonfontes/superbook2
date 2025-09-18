# villains/views.py
from django.shortcuts import render

def lista_viloes(request):
    return render(request, 'villains/lista_viloes.html')

