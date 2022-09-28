from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Erika sigue siendo malvada, ayer me negó aumentarme un cuellito de pollo a mi almuerzo. y en la noche no me ofeció cena. Pero se quedó entre las sobras una presa de pollo entera que era una pierna")
# Create your views here.
