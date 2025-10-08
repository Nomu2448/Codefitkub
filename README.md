---

# 🌸 CodeFitKub

## แพลตฟอร์มดิจิทัลสำหรับการดูแลสุขภาพและฟิตเนส ที่ช่วยให้คุณมีสุขภาพที่ดีขึ้น

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with❤️](https://img.shields.io/badge/Made%20with-❤️-pink.svg)](https://github.com/Nomu2448/Codefitkub)

---

## 👩‍💻 สมาชิกผู้พัฒนา

- 👦 **นายนนทพัทธ์ นะทีศรี** — 6712732108
- 👦 **นายวทัญญู ช่างเกวียน** — 6712732117
- 👩 **นางสาวจีรนันท์ เกิดกล้า** — 6712732121
- 👦 **นายนิลรักษ์ บุตรโพธิ์ศรี** — 6712732130

---

## 📖 เกี่ยวกับโปรเจกต์

✨ **CodeFitKub** เป็นแพลตฟอร์มออนไลน์ที่พัฒนาขึ้นเพื่อช่วยให้ผู้ใช้สามารถติดตามและดูแลสุขภาพของตนเองได้อย่างมีประสิทธิภาพ
เป็นเสมือน _เพื่อนคู่คิดด้านสุขภาพ_ ที่จะช่วยคำนวณค่า BMI และให้คำแนะนำด้านโภชนาการ 🏃‍♂️🥗

---

## ✨ ฟีเจอร์หลัก

- 📊 **เครื่องคำนวณ BMI** — คำนวณและแปลผลค่าดัชนีมวลกาย
- 🥗 **ข้อมูลโภชนาการ** — คำแนะนำด้านอาหารและโภชนาการ
- 👤 **ระบบสมาชิก** — ลงทะเบียนและเข้าสู่ระบบ
- 📱 **Responsive Design** — ใช้งานได้ทุกอุปกรณ์
- 📈 **ติดตามพัฒนาการ** — บันทึกและดูความเปลี่ยนแปลง
- 🔐 **ความปลอดภัย** — ระบบรักษาความปลอดภัยข้อมูล

## โครงสร้างโปรเจค

```
Codefitkub/
├── Codefitkub/              # โฟลเดอร์การตั้งค่าโปรเจค
│   ├── settings.py          # การตั้งค่า Django
│   ├── urls.py              # การกำหนด URL หลัก
│   ├── wsgi.py             # การตั้งค่า WSGI
│   └── asgi.py             # การตั้งค่า ASGI
├── webpage/                 # โฟลเดอร์แอปพลิเคชันหลัก
│   ├── views.py            # ฟังก์ชันควบคุมการแสดงผล
│   ├── models.py           # โมเดลฐานข้อมูล
│   ├── urls.py             # การกำหนด URL ของแอปพลิเคชัน
│   └── admin.py            # การตั้งค่าหน้าผู้ดูแลระบบ
├── templates/              # เทมเพลต HTML
│   ├── base.html          # เทมเพลตหลัก
│   ├── home.html          # หน้าแรก
│   ├── bmi.html           # หน้าคำนวณ BMI
│   ├── login.html         # หน้าเข้าสู่ระบบ
│   ├── register.html      # หน้าลงทะเบียน
│   ├── profile.html       # หน้าโปรไฟล์
│   └── Nutrition.html     # หน้าข้อมูลโภชนาการ
├── statics/               # ไฟล์คงที่
│   └── assets/
│       └── img/          # รูปภาพ
├── public/               # ไฟล์สาธารณะ
├── manage.py            # สคริปต์จัดการ Django
└── requirements.txt     # รายการแพ็คเกจที่จำเป็น
```

## เทคโนโลยีที่ใช้

- Python 3.13
- Django 5.2.7
- ฐานข้อมูล SQLite
- HTML/CSS
- PostgreSQL (psycopg2-binary)

## แพ็คเกจที่จำเป็น

แพ็คเกจหลักที่ใช้ในโปรเจค:

- Django==5.2.7
- psycopg2-binary==2.9.10
- asgiref==3.10.0
- sqlparse==0.5.3
- tzdata==2025.2

## การติดตั้งและการตั้งค่า

1. Create a virtual environment:

   ```
   python -m venv env
   ```

2. Activate the virtual environment:

   - Windows:
     ```
     env\Scripts\activate
     ```
   - Unix or MacOS:
     ```
     source env/bin/activate
     ```

3. Install required packages:

   ```
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## รายละเอียดฟีเจอร์

### เครื่องคำนวณค่า BMI

- คำนวณค่าดัชนีมวลกาย (BMI)
- แปลผลสถานะน้ำหนัก:
  - น้ำหนักน้อย/ผอม: BMI < 18.5
  - ปกติ: BMI 18.5-24.9
  - น้ำหนักเกิน: BMI 25-29.9
  - อ้วน: BMI ≥ 30

### ระบบผู้ใช้

- การลงทะเบียนผู้ใช้
- การเข้าสู่ระบบ
- การจัดการโปรไฟล์

## คำอธิบายโครงสร้างไดเรกทอรี

- `Codefitkub/`: เก็บการตั้งค่าและการกำหนดค่าของโปรเจค
- `webpage/`: ไดเรกทอรีแอปพลิเคชันหลักที่มี views, models และตรรกะทางธุรกิจ
- `templates/`: เทมเพลต HTML สำหรับส่วนติดต่อผู้ใช้
- `statics/`: ไฟล์คงที่รวมถึงรูปภาพและทรัพยากรต่างๆ
- `public/`: ไฟล์สาธารณะที่เข้าถึงได้จากเว็บ
- `env/`: ไดเรกทอรี virtual environment (ไม่ถูกติดตามใน version control)

## การมีส่วนร่วมในการพัฒนา

1. Fork โปรเจค
2. สร้าง branch สำหรับฟีเจอร์ของคุณ
3. Commit การเปลี่ยนแปลง
4. Push ไปยัง branch
5. สร้าง Pull Request

## ลิขสิทธิ์

โปรเจคนี้เป็นโอเพนซอร์สและอยู่ภายใต้ลิขสิทธิ์ MIT License.
