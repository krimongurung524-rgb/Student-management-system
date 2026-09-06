from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# REGISTER VIEW
def register_view(request):
    if request.user.is_authenticated:
        return redirect('student_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created successfully! Please login.")
            return redirect('login_view')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'auth/register.html', {'form': form})


# LOGIN VIEW
def login_view(request):
    if request.user.is_authenticated:
        return redirect('student_list')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('student_list')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})


# LOGOUT VIEW — POST matra (CSRF protection)
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect('login_view')
    return redirect('student_list')