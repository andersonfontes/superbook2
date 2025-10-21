from django.shortcuts import render, redirect
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

