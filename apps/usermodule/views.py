from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('/books/lab11/students/')   # ← المكان اللي ترجعين له بعد النجاح
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'usermodule/login.html')