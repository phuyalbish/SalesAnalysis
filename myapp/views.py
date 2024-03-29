from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.urls import reverse
# from SalesAnalysis.myapp.forms import SignUpForm

def home_index(request):
    return render(request,'myapp/index.html')

def dashboard_view(request):
    return render(request,'myapp/dashboard.html')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['password1']
            pass2 = form.cleaned_data['password2']

            if pass1!=pass2:
                messages.success(request, ("Your password doesnot match"))
                return redirect(reverse('signup'))

            my_user = User.objects.create_user(username, email, pass1)

            try:
                validate_password(pass1, user=my_user)
                my_user.save()

            except ValidationError as e:
                my_user.delete()  # Rollback user creation
                messages.error(request, e)
                return redirect(reverse('signup'))

            messages.success(request, ("Account Registered Successfully!"))
            return redirect(reverse('login'))
        else:
            messages.error(request, "Form is not valid. Please correct the errors.")
            return redirect(reverse('signup'))
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('/')
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect('login')
    else:
        return render(request, 'myapp/login.html')


def log_out(request):
    logout(request)
    return redirect(reverse('/'))
