from django.urls import path
from . import views

urlpatterns = [
    path('', views.countries, name='countries'),
    path('compare_countries/', views.compare_countries, name='compare_countries'),
    path('compare_countries_in_region/', views.compare_countries_in_region, name='compare_countries_in_region'),
    path('countries_in_region/', views.countries_in_region, name='countries_in_region'),
    path('countries_in_income_group/', views.countries_in_income_group, name='countries_in_income_group'),
    path('show/', views.show, name='show'),
    path('about/', views.about, name='about'),
]
