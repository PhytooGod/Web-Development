from django.shortcuts import render
from .models import product
from .models import category

def index(request):
	return render(request, 'api/index.html')

def produ(request):
	products = product.objects.all()
	return render(request, 'api/produ.html', {'products':products})

def catego(request):
	categorys = category.objects.all()
	return render(request, 'api/catego.html', {'categorys':categorys})	

def oneprodu(request, id):
	oneprodu = product.objects.order_by('id')[id-1:id]
	return render(request, 'api/oneprodu.html', {'oneprodu':oneprodu})

def onecatego(request, id):
	onecatego = category.objects.order_by('id')[id-1:id]
	return render(request, 'api/onecatego.html', {'onecatego':onecatego})