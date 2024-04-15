from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Catalyst_User
from django.urls import reverse
from django.contrib import messages



def signup(request, template_name='login_signup/signup.html'):
    if request.method == 'POST':
        postdata = request.POST.copy()
        first_name = postdata.get('fname')
        last_name = postdata.get('lname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')
        username = postdata.get('username')

        if Catalyst_User.objects.filter(user_name=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, template_name, locals())

        user=Catalyst_User(firt_name=first_name,last_name=last_name,phone=phone,email=email,password=password,user_name=username)
        user.password=make_password(user.password)
        user.register()

        url = reverse('upload_data:upload_data')
        return HttpResponseRedirect(url)

    return render(request,template_name,locals())

def login(request, template_name='login_signup/login.html'):
    if request.method == 'POST':
        postdata = request.POST.copy()
        username = postdata.get('username')
        password = postdata.get('password')
        user = Catalyst_User.get_user_by_username(username)

        error_message=None

        if user:
            user_authentication=check_password(password,user.password)
            if user_authentication:
                request.session['customer_id']=user.id
                request.session['email']=user.email
                url = reverse('upload_data:upload_data')
                return HttpResponseRedirect(url)
            else:
                error_message="Username or Password Invalid !!"
        else:
            error_message="Username or Password Invalid !!"

    return render(request,template_name,locals())


def LogoutUser(request):
    logout(request)
    url = reverse('login_signup:login')
    return HttpResponseRedirect(url)
