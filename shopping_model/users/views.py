from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
# Create your views here.

def register(request):
    if request.method=='POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
         form = RegisterationForm()
    return render (request,'users/register.html',{'form':form})

#
#
# def login(request):
#     if request.method=='POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('food:index')
#             else:
#                 return redirect('register')
#             # Redirect to a success page.
#     else:
#         form = LoginForm()
#     return render (request,'users/login.html',{'form':form})    # Return an 'invalid login' error message.
