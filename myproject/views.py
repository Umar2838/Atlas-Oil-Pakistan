from django.shortcuts import render,redirect
from myapp.models import SubmittedCode
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")
def submitcode(request):
    return render(request, "submitcode.html")
def adminlogin(request):
    return render(request, "adminlogin.html")
def adminpanel(request):
    return render(request, "adminpanel.html")

def submitcode(request):
    if request.method == 'POST':
        code = request.POST.get('contact')

        if code and len(code) == 5:
            SubmittedCode.objects.create(code=code)
   

    return render(request, 'submitcode.html')

def admin_panel(request):
    codes = SubmittedCode.objects.all() 
    return render(request, 'adminpanel.html', {'codes': codes})

def get_submitted_codes(request):
    codes = SubmittedCode.objects.all().values('code', 'created_at')
    codes_list = list(codes)  # Convert QuerySet to a list
    return JsonResponse(codes_list, safe=False)