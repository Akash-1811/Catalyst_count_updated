from django.urls import path
from upload_data import views

app_name = 'upload_data'

urlpatterns = [
    path('upload_data/', views.upload_data,name='upload_data'),
    path('query_builder/', views.query_builder_view,name='query_builder_view'),
    ]