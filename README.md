<!-- 🌤 แบนเนอร์แนวสุขภาพ -->
<p align="center">
<img width="1755" height="1008" alt="pw-web" src="https://github.com/user-attachments/assets/d05231f5-3b8f-4c2d-a35c-1779915002af" />


# 🩵 CodeFitKub

> **แพลตฟอร์มสุขภาพและฟิตเนสออนไลน์**  
> ที่ช่วยให้คุณคำนวณ BMI, ดูข้อมูลโภชนาการ และติดตามพัฒนาการของสุขภาพได้ง่าย ๆ  
> 💙 สุขภาพดี เริ่มต้นได้ที่นี่!

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-❤️-pink.svg)](https://github.com/Nomu2448/Codefitkub)
[![Build with Django](https://img.shields.io/badge/Build%20with-Django-green.svg)](https://www.djangoproject.com/)
[![Deploy on Vercel](https://img.shields.io/badge/Deploy-Vercel-black.svg)](https://vercel.com)

---

## 👩‍💻 ทีมผู้พัฒนา

| ชื่อ | รหัสนักศึกษา |
|------|----------------|
| 👦 นายนนทพัทธ์ นะทีศรี | 6712732108 |
| 👦 นายวทัญญู ช่างเกวียน | 6712732117 |
| 👩 นางสาวจีรนันท์ เกิดกล้า | 6712732121 |
| 👦 นายนิลรักษ์ บุตรโพธิ์ศรี | 6712732130 |
---

## 📖 เกี่ยวกับโปรเจกต์

**CodeFitKub** เป็นเว็บแอปพลิเคชันที่ถูกพัฒนาด้วย Django Framework  
เพื่อช่วยให้ผู้ใช้งานสามารถติดตามสุขภาพของตนเองได้อย่างง่ายดาย  
เช่น การคำนวณ BMI, การรับคำแนะนำด้านโภชนาการ, และการจัดการโปรไฟล์ส่วนตัว  

ออกแบบให้ **ใช้งานได้ทุกอุปกรณ์** (Responsive Design)  
และเน้นความปลอดภัยของข้อมูลผู้ใช้เป็นหลัก 🔒

---

## ✨ ฟีเจอร์หลัก

- 📊 **คำนวณค่า BMI** — แสดงผลและแนะนำตามเกณฑ์สุขภาพ  
- 🥗 **ข้อมูลโภชนาการ** — แนะนำอาหารตามผลลัพธ์ BMI  
- 👤 **ระบบสมาชิก** — สมัคร / เข้าสู่ระบบ / โปรไฟล์ส่วนตัว  
- 📈 **บันทึกพัฒนาการสุขภาพ** — ดูการเปลี่ยนแปลงของร่างกาย  
- 📱 **Responsive Design** — ใช้งานได้บนมือถือและคอมพิวเตอร์  
- 🔒 **ระบบความปลอดภัย** — ใช้ Django Auth และการเข้ารหัส  

---

## 🛠 เทคโนโลยีที่ใช้

| หมวด | เทคโนโลยี |
|-------|-------------|
| 🐍 Backend | Python 3.13, Django 5.2.7 |
| 💾 Database | PostgreSQL (ผ่าน Supabase) |
| 🎨 Frontend | HTML5, CSS3, JavaScript |
| ☁️ Hosting | Vercel |
| ⚙️ Tools | Git, Virtual Environment |

---

## 📁 โครงสร้างโปรเจกต์

Codefitkub/
├── Codefitkub/ # การตั้งค่าโปรเจกต์ Django
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── webpage/ # แอปหลัก
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│ └── admin.py
├── templates/ # HTML Templates
│ ├── base.html
│ ├── home.html
│ ├── bmi.html
│ ├── login.html
│ ├── register.html
│ ├── profile.html
│ └── nutrition.html
├── static/ # ไฟล์คงที่ เช่น CSS / JS / รูปภาพ
│ └── img/
├── manage.py
└── requirements.txt


---

## ⚙️ การติดตั้งและใช้งาน

### 1️⃣ สร้าง Virtual Environment
```bash
python -m venv env

2️⃣ เปิดใช้งาน Virtual Environment

Windows
env\Scripts\activate
macOS/Linux
source env/bin/activate

3️⃣ ติดตั้งแพ็คเกจที่จำเป็น
pip install -r requirements.txt

4️⃣ รันฐานข้อมูล
python manage.py migrate

5️⃣ เริ่มต้นเซิร์ฟเวอร์
python manage.py runserver

เปิดเบราว์เซอร์และเข้าที่ http://127.0.0.1:8000

☁️ การ Deploy บน Vercel

สมัครบัญชี Vercel
 และเชื่อมต่อกับ GitHub

เพิ่ม Environment Variables ที่จำเป็น เช่น:

DJANGO_SECRET_KEY

SUPABASE_URL

SUPABASE_KEY

🤝 การมีส่วนร่วม (Contributing)

Fork โปรเจกต์

สร้าง branch ใหม่:

git checkout -b feature/ชื่อฟีเจอร์


Commit และ Push

ส่ง Pull Request มาที่ repository หลัก

💡 แนวคิดการออกแบบ

“สุขภาพดีไม่ใช่เรื่องยาก — ถ้ามีเครื่องมือดี ๆ อยู่ใกล้ตัว”
CodeFitKub ถูกออกแบบให้ใช้งานง่าย สีฟ้า–ขาวให้ความรู้สึกสดชื่น
สื่อถึงสุขภาพ ความสะอาด และพลังบวก 💙

🔒 License

โปรเจกต์นี้เผยแพร่ภายใต้ MIT License
สามารถนำไปใช้ ปรับแต่ง หรือพัฒนาต่อยอดได้โดยอิสระ

© 2025 — Developed with ❤️ by Team CodeFitKub
