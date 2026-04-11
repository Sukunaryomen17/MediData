from django.shortcuts import render

# Create your views here.
# MediData/views.py

def home(request):
    # This is where you'll eventually add: 
    # data = MyModel.objects.all()
    context = {
        'title': 'Welcome to MediData',
        'status': 'System Online',
    }
    return render(request, 'MediData/home.html', context)
