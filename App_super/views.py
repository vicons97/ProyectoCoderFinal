
from django.http import HttpResponse
from django.shortcuts import render

def inicio(self):
    
    return render(self, "inicio.html")

