from django.urls import path
from . import views

urlpatterns = [
    path('', views.countries, name='countries'),
    path('income_groups/', views.income_groups, name='income_groups'),
    path('regions/', views.regions, name='regions')
]

