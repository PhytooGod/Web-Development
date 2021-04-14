from django.urls import path
from . import views
urlpatterns = [
    path('companies/', views.companies),
    path('vacancies/', views.vacancies),
    path('companies/<int:id>/', views.onecompany),
    path('companies/<int:id>/vacancies/', views.listofvacancies),
    path('vacancies/<int:id>/', views.onevacancy),
    path('vacancies/top_ten/', views.topvacancies),
]
