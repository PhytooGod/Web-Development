from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('products/', views.produ),
    path('categorys', views.catego),
    path('products/<int:id>/', views.oneprodu),
    path('categorys/<int:id>/', views.onecatego)
]
