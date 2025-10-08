from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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

def nutrition_view(request):
    return render(request, 'nutrition.html')

@login_required
def profile(request):
    # pass the currently logged in user to the template
    return render(request, 'profile.html', {'user': request.user})


def login_view(request):
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        password = request.POST.get('password') or ''

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'เข้าสู่ระบบสำเร็จ')
            return redirect('home')
        else:
            messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง')
            return render(request, 'login.html')

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        username = (request.POST.get('username') or '').strip()
        email = (request.POST.get('email') or '').strip()
        password = request.POST.get('password') or ''
        confirm = request.POST.get('confirmPassword') or ''

        # basic validation
        if not username or not email or not password:
            messages.error(request, 'กรุณากรอกข้อมูลให้ครบถ้วน')
            return render(request, 'register.html')

        if password != confirm:
            messages.error(request, 'รหัสผ่านไม่ตรงกัน')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'มีชื่อผู้ใช้นี้อยู่แล้ว โปรดเลือกชื่ออื่น')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'อีเมลนี้ถูกใช้งานแล้ว')
            return render(request, 'register.html')

        # create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # log the user in and redirect to home
        login(request, user)
        messages.success(request, 'สมัครสมาชิกสำเร็จ ยินดีต้อนรับ')
        return redirect('home')

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'ออกจากระบบเรียบร้อยแล้ว')
    return redirect('login')

