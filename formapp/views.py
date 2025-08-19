from django.shortcuts import render,redirect
from .forms import contactform,loginform

def contact_view(request):
    if request.method == "POST":
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_view')
    else:
            form = contactform()
            return render(request, 'contact.html', {'form': form})


# Create your views here.

def login_view(request):
     if request.method == "POST":
          form = loginform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('login_view')
     else:
                form = loginform()
                return render(request, 'login.html', {'form': form})
