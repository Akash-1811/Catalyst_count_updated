from django.test import TestCase
from django.urls import reverse
from .models import Companies
from rest_framework.test import APIClient
import requests


class QueryBuilderAPITestCase(TestCase):
    def setUp(self):
        # Initialize the API client
        self.client = APIClient()

    def test_query_builder_api(self):
        # Define test data
        Companies.objects.create(company_name='Test Company', industry='Technology', locality='San Francisco, CA, USA')

        # Generate the URL for your view function
        url = reverse('upload_data:query_builder_view')

        # Define test data
        industry = 'Technology'
        state = 'CA'
        city = 'San Francisco'
        country = 'USA'
        employee_from = '100'
        employee_to = '1000'
        search_keyword = 'software'

        # Make a POST request to the view function
        response = self.client.post(url, {
            'industry': industry,
            'state': state,
            'city': city,
            'country': country,
            'employee_from': employee_from,
            'employee_to': employee_to,
            'search_keyword': search_keyword
        })

        # Assert that the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check the content of the response JSON
        response_data = response.json()
        self.assertEqual(response_data['status'], 'success')
        self.assertEqual(response_data['code'], '200')
        self.assertIn('data', response_data)
        self.assertIn('Result Count', response_data['data'])

        # Get the count from the response data
        result_count = response_data['data']['Result Count']

        # Assert that the result count is as expected
        # Add more assertions here based on your expected result count
        self.assertTrue(result_count > 0)


class YourTestSuite(TestCase):
    def test_query_builder(self):
        query_builder_test_case = QueryBuilderAPITestCase()
        query_builder_test_case.test_query_builder_api()
