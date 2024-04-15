from django.urls import path,include
from upload_data import api

app_name = 'upload_data_api'

urlpatterns = [
    path('api/v1/upload_data_api/', api.query_builder,name='query_builder'),
    ]

