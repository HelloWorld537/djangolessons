from django.http import HttpResponse
from django.shortcuts import render

def firstPage(request):
    return render(request, '/index.html')