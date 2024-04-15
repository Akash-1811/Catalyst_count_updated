from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Companies

@api_view(['GET'])
def query_builder(request):
    # Get filter parameters from request query parameters
    industry = request.GET.get('industry')
    state = request.GET.get('state')
    city = request.GET.get('city')
    country = request.GET.get('country')
    employee_from = request.GET.get('employee_from')
    employee_to = request.GET.get('employee_to')
    search_keyword = request.GET.get('search_keyword')

    queryset = Companies.objects.all()

    if industry:
        queryset = queryset.filter(industry=industry)
    if state:
        queryset = queryset.filter(locality__icontains=state)  # Assuming state is in locality field
    if city:
        queryset = queryset.filter(locality__icontains=city)  # Assuming city is in locality field
    if country:
        print(country,'country')
        queryset = queryset.filter(country=country)
        print(len(queryset),'len_queryset')
    if employee_from:
        employee_from = int(employee_from.replace(',', ''))
        queryset = queryset.filter(total_employee_est__gte=employee_from)
    if employee_to:
        employee_to = int(employee_to.replace(',', ''))
        queryset = queryset.filter(total_employee_est__lte=employee_to)
    if search_keyword:
        queryset = queryset.filter(company_name__icontains=search_keyword)

    result_count = queryset.count()

    # Return the result count as a JSON response
    data = {'Result Count': result_count}
    message = "Result Count Fetched"
    return Response({'status': 'success', 'code': '200', 'data': data, 'message': message})
