from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.views.decorators.http import require_GET

from .models import Company, People

import json


@require_GET
def get_company(request, company):
    print("company=", company)
    company_qs = Company.objects.filter(company=company)               
    if company_qs:
        people_list = []
        for c in company_qs:
            people_qs = People.objects.filter(company_id=c.index)
            for p in people_qs:
                people_list.append(model_to_dict( p ))

        return JsonResponse({ "employees": people_list}, status=200)

    else:
        return JsonResponse({ "error": "Company not found." }, status=404)



@require_GET
def get_people(request, name):
    print("name=", name)

    name_list = name.split(',')

    data = {}
    if len(name_list) == 1:
        data = People.get_one(name)
    else:
        data = People.get_multi(name_list)

    if data:
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({ "error": "Name not found." }, status=404)


def return_404_error(request, exception):
    return JsonResponse({ "error": "Invalid URL" }, status=404)

def return_500_error(request):
    return JsonResponse({ "error": "Internal error" }, status=500)
