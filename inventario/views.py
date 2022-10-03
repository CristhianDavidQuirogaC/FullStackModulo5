from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria

# Create your views here.

def index(request):
	return HttpResponse("Erika sigue siendo malvada, ayer me negó aumentarme un cuellito de pollo a mi almuerzo. y en la noche no me ofeció cena. Pero se quedó entre las sobras una presa de pollo entera que era una pierna")

def contacto(request, nombre):
	return HttpResponse(f"Parece que: {nombre} Erika esta cambiando un poco Che ")

def categoria(request):
	categorias = Categoria.objects.all()
	return render(request,"categorias.html",{"categorias":categorias})
	