from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    if request.user.is_authenticated:
        return redirect('add_needy')

    message = None
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(request, username=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('add_needy')
        else:
            message = "نام کاربری یا رمز عبور اشتباه است."
    return render(request, 'accounts/login.html', {'message': message})
