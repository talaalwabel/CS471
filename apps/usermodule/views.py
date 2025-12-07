from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('/users/register')

        User.objects.create_user(username=username, password=password)
        messages.success(request, "You have successfully registered!")
        return redirect('/users/login')

    return render(request, 'usermodule/register.html')
