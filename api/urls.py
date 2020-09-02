from django.contrib import admin
from django.urls import path

from .views import get_company, get_people

urlpatterns = [
    path('company/<str:company>', get_company, name="get_company"),
    path('people/<str:name>', get_people, name="get_people"),
]

