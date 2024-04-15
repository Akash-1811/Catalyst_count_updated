from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
import csv
import traceback
from upload_data.models import Companies
from django.db import transaction
import requests
from rest_framework.test import APIClient
from django.test import TestCase
from upload_data.test import QueryBuilderAPITestCase

from django import forms

class UploadForm(forms.Form):
    upload_csv = forms.FileField(label='Upload CSV')


@transaction.atomic
def upload_data(request, template_name='upload_data/upload_data.html'):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['upload_csv']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Please upload a CSV file.')
                return HttpResponseRedirect(reverse('upload_data:upload_data'))

            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.reader(decoded_file)

                companies_to_create = []
                for row_number, row in enumerate(reader, start=1):
                    # Handle empty fields by setting default values
                    row += [''] * (11 - len(row))  # Fill empty fields with empty strings

                    company = Companies(
                        company_id=row[0],
                        company_name=row[1],
                        company_domain=row[2],
                        year_founded=row[3],
                        industry=row[4],
                        size_range=row[5],
                        locality=row[6],
                        country=row[7],
                        linked_in_url=row[8],
                        current_employee_est=row[9],
                        total_employee_est=row[10]
                    )
                    companies_to_create.append(company)

                # Bulk create the objects
                Companies.objects.bulk_create(companies_to_create)

                messages.success(request, 'CSV file uploaded successfully.')
                return HttpResponseRedirect(reverse('upload_data:upload_data'))
            except Exception as e:
                messages.error(request, f'Error occurred: {e}')
                print("Error occurred:", e)
                print(traceback.format_exc())  # Print the full traceback
    else:
        form = UploadForm()

    return render(request,template_name,locals())

def query_builder_view(request,template_name = 'upload_data/query_builder.html'):
    result_count = Companies.objects.all().values('id').count()
    countries = Companies.objects.all().values_list('country',flat=True).distinct()
    localities = Companies.objects.exclude(locality='').values_list('locality', flat=True).distinct()
    industries = Companies.objects.all().values_list('industry', flat=True).distinct()
    sliced_cities = []
    for locality in localities:
        if locality:
            city = locality.split(',')[0].strip()
            sliced_cities.append(city)
    sliced_cities = sliced_cities[0:30]
    print(sliced_cities)
    if request.method == 'POST':
        industry = request.POST.get('industry')
        state = request.POST.get('state')
        city = request.POST.get('city')
        country = request.POST.get('country')
        employee_from = request.POST.get('employee_from')
        employee_to = request.POST.get('employee_to')
        search_keyword = request.POST.get('search_keyword')
        api_relative_url = 'upload_data_api/api/v1/upload_data_api/'
        api_url = 'http://127.0.0.1:8000/' + api_relative_url
        payload = {
            'industry': industry,
            'state': state,
            'city': city,
            'country': country,
            'employee_from': employee_from,
            'employee_to': employee_to,
            'search_keyword': search_keyword
        }
        response = requests.get(api_url, params=payload)
        print(response.json())
        response_data = response.json()
        try:
            result_count = response_data['data']['Result Count']
        except Exception as e:
            result_count = 0

    return render(request, template_name, locals())

