from django.urls import path
from login_signup import views

app_name = 'login_signup'

urlpatterns = [
    # path('index/', views.index),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.LogoutUser),
    ]