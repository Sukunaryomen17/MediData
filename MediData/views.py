from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile

# Create your views here.
# MediData/views.py

def home(request):
    if request.user.is_authenticated:
        display_title = f"Dashboard for {request.user.first_name}"
    else:
        display_title = "Welcome to MediData"

    context = {
        'title': display_title,
        'status': 'System Online',
    }
    return render(request, 'MediData/home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # 1. Create the User
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            # Split full_name into first/last for Django's internal fields
            names = form.cleaned_data['full_name'].split(' ', 1)
            user.first_name = names[0]
            user.last_name = names[1] if len(names) > 1 else ""
            user.save()

            # 2. Create the Profile (for DOB)
            Profile.objects.create(user=user, dob=form.cleaned_data['dob'])
            
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'MediData/register.html', {'form': form})
