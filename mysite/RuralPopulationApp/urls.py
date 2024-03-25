from django.urls import path
from . import views

urlpatterns = [
    path('', views.countries, name='countries'),
    path('compare_countries/', views.compare_countries, name='compare_countries'),
    path('compare_countries_in_region/', views.compare_countries_in_region, name='compare_countries_in_region'),
    path('compare_countries_in_income_group/', views.compare_countries_in_income_group, name='compare_countries_in_income_group'),
    path('show/', views.show, name='show'),
]
