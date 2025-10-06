from django.shortcuts import render
from . import views
# Create your views here.

def home(request):
    return render(request, 'home.html')

def bmi(request):
    bmi = None
    status = None
    if request.method == 'POST':
        try:
            height = float(request.POST.get('height')) / 100
            weight = float(request.POST.get('weight'))
            bmi = round(weight / (height ** 2), 2)
            if bmi < 18.5:
                status = 'น้ำหนักน้อย/ผอม'
            elif bmi < 25:
                status = 'ปกติ'
            elif bmi < 30:
                status = 'น้ำหนักเกิน'
            else:
                status = 'อ้วน'
        except Exception:
            bmi = None
            status = 'ข้อมูลไม่ถูกต้อง'
    return render(request, 'bmi.html', {'bmi': bmi, 'status': status})

def nutrition(request):
    return render(request, 'nutrition.html')

def profile(request):
    return render(request, 'profile.html')