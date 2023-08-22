from userauth.models import loginContent, registerContent
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.decorators import user_passes_test

# def register_request(request):
#     register_content = registerContent.objects.all
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#             messages.success(request, f'Your account has been created, You can log in now!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#
#     return render(request, 'register_request.html', context={"register_content":register_content, 'form': form})
#

# @user_passes_test(lambda user: not user.username, login_url='login_request', redirect_field_name=None)
def register_request(request):
    register_content = registerContent.objects.all
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home_view')
    else:
        form = RegisterUserForm()
    return render(request, "register_request.html", {'form':form, "register_content":register_content})

# def login_request(request):
#     login_content = loginContent.objects.all
#     return render(request, 'login_request.html', context={"login_content": login_content})

# @user_passes_test(lambda user: not user.username, login_url='login_request', redirect_field_name=None)
def login_request(request):
    login_content = loginContent.objects.all
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_view')
        else:
            messages.success(request, ("Username or Password is incorrect, Try again!"))
            return redirect('login_request')
    else:
        return render(request, 'login_request.html',{"login_content": login_content})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were Logged Out!"))
    return redirect('login_request')