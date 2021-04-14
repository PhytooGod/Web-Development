from django.shortcuts import render
from .models import Company
from .models import Vacancy

def companies(request):
	companies = Company.objects.all()
	return render(request, 'api/companies.html', {'companies':companies	})

def vacancies(request):
	vacancies = Vacancy.objects.all()
	return render(request, 'api/vacancies.html', {'vacancies':vacancies})

def onecompany(request, id):
	onecompany = Company.objects.order_by('id')[id-1:id]
	return render(request, 'api/companies.html', {'companies':onecompany})

def listofvacancies(request, id):
	listofvacancies = Vacancy.objects.filter(company=id)
	return render(request, 'api/vacancies.html', {'vacancies':listofvacancies})

def onevacancy(request, id):
	onevacancy = Vacancy.objects.order_by('id')[id-1:id]
	return render(request, 'api/vacancies.html', {'vacancies':onevacancy})

def topvacancies(request):
	topvacancies = Vacancy.objects.order_by('salary').reverse()[:10]
	return render(request, 'api/vacancies.html', {'vacancies':topvacancies})