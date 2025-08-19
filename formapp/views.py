from django.shortcuts import render, redirect
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Basic validation
        if password != confirm_password:
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})

        # Check if username (which is email) already exists
        if User.objects.filter(username=email).exists():
            return render(request, 'signup.html', {'error_message': 'Email already exists'})

        try:
            # Create user, setting username to email
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = fullname
            user.save()

            # Create profile linked to user
            UserProfile.objects.create(user=user, mobile=mobile)

            # Log the user in immediately (optional)
            login(request, user)

            # Redirect to login page or home page as you want
            return redirect('user_login')

        except Exception as e:
            # Log the error for debugging and show a friendly message
            print(f"Error creating user or profile: {e}")
            return render(request, 'signup.html', {'error_message': 'An error occurred during registration. Please try again.'})

    # If GET request, just render signup form
    return render(request, 'signup.html')



def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # authenticate expects username, which you set as email
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')
