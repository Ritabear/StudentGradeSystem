import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from authen.forms import RegisterUserForm


#https://docs.djangoproject.com/en/4.2/topics/auth/default/#auth-web-requests
def loginUser(request):
    print(request)#<WSGIRequest: GET '/authen/login_user/'>
    if request.method == "POST": #!
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home")
        else:
            messages.error(request, "Username or password is incorrect")
            return render(request, "authenticate/Login.html",{})
            # return redirect('login')
            # The view authen.views.loginUser didn't return an HttpResponse object. It returned None instead.

            # #urlpatterns name #use name of a view declared in url to redirect to that specific page
    else:
        return render(request, "authenticate/Login.html",{})


def logoutUser(request):
    if request.user:
        logout(request)
        messages.success(request, ("You Were Logged Out!"))
    else:
        messages.error(request, ("You Are Not Logged In!"))
    return redirect('home')


def registerUser(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            #!

            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/RegisterUser.html', {
        'form':form,
    })
