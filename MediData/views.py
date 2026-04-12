from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile
import requests
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import PDFUploadForm
from .models import AnalysisResult

# Replace with your actual external model URL
MODEL_API_URL = "http://13.206.108.88:8000/extract-from-file"

from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json


@require_POST
def analyse_pdf(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'You must be logged in to analyse a PDF.'}, status=401)

    form = PDFUploadForm(request.POST, request.FILES)
    if not form.is_valid():
        return JsonResponse({'error': 'Invalid form submission.'}, status=400)

    pdf_file = request.FILES['file']

    try:
        files = {'file': (pdf_file.name, pdf_file.read(), 'application/pdf')}
        response = requests.post(MODEL_API_URL, files=files, timeout=60)
        response.raise_for_status()
        raw_json = response.json()
    except requests.Timeout:
        return JsonResponse({'error': 'The analysis server timed out. Please try again.'}, status=504)
    except requests.RequestException as e:
        return JsonResponse({'error': f'Could not reach analysis server: {str(e)}'}, status=502)

    # Check API-level error field
    if not raw_json.get('is_success'):
        error_msg = raw_json.get('error') or 'Analysis failed.'
        return JsonResponse({'error': error_msg}, status=500)

    data = raw_json.get('data', {})

    # Flatten all bill_items across pages into a single list
    all_items = []
    for page in data.get('pagewise_line_items', []):
        for item in page.get('bill_items', []):
            all_items.append({
                'item_name': item.get('item_name', ''),
                'quantity':  item.get('item_quantity', 1),
                'rate':      item.get('item_rate', 0),
                'amount':    item.get('item_amount', 0),
            })

    result_payload = {
        'line_items':   all_items,
        'final_total':  data.get('grand_total', 0),
        'item_count':   data.get('total_item_count', len(all_items)),
        'error_flag':   raw_json.get('error'),   # None means no error
    }

    # Save to DB
    pdf_file.seek(0)
    AnalysisResult.objects.create(
        user=request.user,
        pdf_file=pdf_file,
        original_filename=pdf_file.name,
        result=result_payload,
    )

    return JsonResponse({
        'filename': pdf_file.name,
        'data': result_payload,
    })


def home(request):
    context = {
        'title': f"Dashboard for {request.user.first_name}" if request.user.is_authenticated else "Welcome to MediData",
        'status': 'System Online',
    }
    return render(request, 'MediData/home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            names = form.cleaned_data['full_name'].split(' ', 1)
            user.first_name = names[0]
            user.last_name = names[1] if len(names) > 1 else ""
            user.save()
            Profile.objects.create(user=user, dob=form.cleaned_data['dob'])
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'MediData/register.html', {'form': form})
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
