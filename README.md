<p align="center">
  <img width="1584" alt="CodeFitKub Banner 3" src="https://github.com/user-attachments/assets/84e3c4ae-9ff8-424c-9cef-2bf2b630e18f" />
  <img width="1584" alt="CodeFitKub Banner 1" src="https://github.com/user-attachments/assets/82213bdf-7eaa-4592-89d3-0334ac9ada3c" />
  <img width="1584" alt="CodeFitKub Banner 2" src="https://github.com/user-attachments/assets/9a8d5e66-b654-476e-b2ec-b3c2d3342255" />
 
</p>

<h1 align="center">🩵 CodeFitKub</h1>

<p align="center">
  <strong>แพลตฟอร์มสุขภาพและฟิตเนสออนไลน์</strong>
</p>

<p align="center">
  ที่ช่วยให้คุณคำนวณ BMI, จัดการโปรแกรมออกกำลังกาย, ดูข้อมูลโภชนาการ<br>
  และติดตามพัฒนาการของสุขภาพได้ง่าย ๆ<br>
  💙 <em>สุขภาพดี เริ่มต้นได้ที่นี่!</em>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/Django-5.2.7-green.svg" alt="Django"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.13+-blue.svg" alt="Python"></a>
  <a href="https://vercel.com"><img src="https://img.shields.io/badge/Deploy-Vercel-black.svg" alt="Vercel"></a>
  <img src="https://img.shields.io/badge/Made%20with-❤️-pink.svg" alt="Made with Love">
</p>

---

## 📖 เกี่ยวกับโปรเจกต์

**CodeFitKub** เป็นเว็บแอปพลิเคชันที่พัฒนาด้วย Django Framework เพื่อช่วยให้ผู้ใช้งานสามารถดูแลและติดตามสุขภาพของตนเองได้อย่างครอบคลุม ตั้งแต่การคำนวณ BMI, การจัดการโปรแกรมออกกำลังกาย, การบันทึกผลการออกกำลังกาย, ไปจนถึงการรับคำแนะนำด้านโภชนาการ

ออกแบบมาให้ **ใช้งานง่าย ทุกอุปกรณ์** (Responsive Design) และเน้นความปลอดภัยของข้อมูลผู้ใช้เป็นหลัก 🔒

### 💡 แนวคิด
> "สุขภาพดีไม่ใช่เรื่องยาก — ถ้ามีเครื่องมือดี ๆ อยู่ใกล้ตัว"

CodeFitKub ถูกออกแบบด้วยสีโทนฟ้า–ขาวให้ความรู้สึกสดชื่น สื่อถึงสุขภาพ ความสะอาด และพลังบวก 💙

---

## ✨ ฟีเจอร์หลัก

### 👤 1. ระบบจัดการสมาชิก
- สมัครสมาชิกและเข้าสู่ระบบอย่างปลอดภัย
- จัดการโปรไฟล์ส่วนตัว
- ระบบ Authentication ด้วย Django Auth

### 💪 2. การจัดการการออกกำลังกาย
- **ท่าออกกำลังกาย (Exercise)**
  - บันทึกท่าออกกำลังกายพร้อมรายละเอียด (รูปภาพ, คำอธิบาย, วิดีโอ)
  - แบ่งประเภทตามส่วนของร่างกาย (แขน, ขา, อก, หลัง, ไหล่, หน้าท้อง)
  - ระดับความยาก (เริ่มต้น, ปานกลาง, ยาก)

- **โปรแกรมออกกำลังกาย (Workout Program)**
  - สร้างและปรับแต่งโปรแกรมการออกกำลังกายส่วนตัว
  - กำหนดเป้าหมาย (ลดน้ำหนัก, เพิ่มกล้ามเนื้อ, เสริมความแข็งแรง, ความอดทน, ฯลฯ)
  - เลือกท่าออกกำลังกายที่ต้องการรวมเข้าในโปรแกรม

- **บันทึกการออกกำลังกาย (Workout Log)**
  - บันทึกการออกกำลังกายในแต่ละครั้ง
  - ระบุวันที่, ระยะเวลา, โปรแกรมที่ใช้
  - บันทึกรายละเอียดของแต่ละท่า (จำนวนเซ็ต, จำนวนครั้ง, น้ำหนักที่ใช้)
  - ติดตามความก้าวหน้าและพัฒนาการ

### 🏥 3. เครื่องมือสุขภาพ
- **เครื่องคำนวณ BMI**
  - คำนวณค่า BMI จากน้ำหนักและส่วนสูง
  - แสดงผลการประเมิน (น้ำหนักน้อย/ผอม, ปกติ, น้ำหนักเกิน, อ้วน)
  - แนะนำแนวทางการดูแลสุขภาพตามผลลัพธ์

- **ข้อมูลโภชนาการ**
  - แนะนำอาหารตามผลลัพธ์ BMI
  - แสดงข้อมูลโภชนาการที่เป็นประโยชน์

### 📈 4. ติดตามพัฒนาการ
- บันทึกประวัติการออกกำลังกาย
- ดูการเปลี่ยนแปลงของร่างกายเมื่อเวลาผ่านไป
- วิเคราะห์ความก้าวหน้าตามเป้าหมาย

---

## 🛠 เทคโนโลยีที่ใช้

| หมวด | เทคโนโลยี |
|-------|-----------|
| 🐍 **Backend** | Python 3.13, Django 5.2.7 |
| 💾 **Database** | PostgreSQL (ผ่าน Supabase) |
| 🎨 **Frontend** | HTML5, CSS3, JavaScript |
| 🎯 **UI Framework** | Bootstrap / Custom CSS |
| ☁️ **Hosting** | Vercel |
| ⚙️ **Tools** | Git, Virtual Environment, pip |

---

## 📁 โครงสร้างโปรเจกต์

```
Codefitkub/
├── Codefitkub/              # การตั้งค่าโปรเจกต์ Django
│   ├── settings.py          # การตั้งค่าหลัก (Database, Apps, Middleware)
│   ├── urls.py              # URL routing หลัก
│   ├── wsgi.py              # WSGI configuration สำหรับ production
│   └── asgi.py              # ASGI configuration
├── webpage/                 # แอปหลัก
│   ├── models.py            # โมเดลฐานข้อมูล (User, Exercise, WorkoutProgram, etc.)
│   ├── views.py             # Views และ Business Logic
│   ├── urls.py              # URL patterns ของแอป
│   ├── forms.py             # Django Forms
│   └── admin.py             # การตั้งค่า Django Admin
├── templates/               # HTML Templates
│   ├── base.html            # Template หลัก
│   ├── home.html            # หน้าแรก
│   ├── bmi.html             # หน้าคำนวณ BMI
│   ├── login.html           # หน้าเข้าสู่ระบบ
│   ├── register.html        # หน้าสมัครสมาชิก
│   ├── profile.html         # หน้าโปรไฟล์ผู้ใช้
│   └── nutrition.html       # หน้าข้อมูลโภชนาการ
├── static/                  # ไฟล์คงที่
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   └── img/                 # รูปภาพและ assets
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── vercel.json              # Vercel deployment configuration
└── .env                     # Environment variables (ไม่ commit ใน Git)
```

---

## ⚙️ การติดตั้งและใช้งาน

### 📋 ความต้องการของระบบ
- **Python** 3.13 หรือสูงกว่า
- **Django** 5.2.7 หรือสูงกว่า
- **PostgreSQL** (ผ่าน Supabase)
- **pip** (Python package manager)
- **Git** (สำหรับ clone repository)

### 🚀 ขั้นตอนการติดตั้ง

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/Nomu2448/Codefitkub.git
cd Codefitkub
```

#### 2️⃣ สร้าง Virtual Environment
```bash
# สร้าง virtual environment
python -m venv env

# เปิดใช้งาน virtual environment
# Windows:
env\Scripts\activate

# macOS/Linux:
source env/bin/activate
```

#### 3️⃣ ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

#### 4️⃣ ตั้งค่า Environment Variables
สร้างไฟล์ `.env` ในโฟลเดอร์หลักของโปรเจกต์:

```env
# Database Configuration (Supabase)
SUPABASE_DB_PASSWORD=your_supabase_password

# Django Secret Key
DJANGO_SECRET_KEY=your_secret_key_here

# Debug Mode (ตั้งเป็น False ใน production)
DEBUG=True

# Allowed Hosts (แก้ไขตาม domain ของคุณ)
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### 5️⃣ รัน Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 6️⃣ สร้าง Superuser (Optional)
```bash
python manage.py createsuperuser
```

#### 7️⃣ รันเซิร์ฟเวอร์
```bash
python manage.py runserver
```

เปิดเบราว์เซอร์และเข้าใช้งานที่ **http://127.0.0.1:8000** 🎉

---

## ☁️ การ Deploy บน Vercel

### วิธี Deploy ด้วย Vercel CLI

1. **ติดตั้ง Vercel CLI**
```bash
npm install -g vercel
```

2. **Login เข้า Vercel**
```bash
vercel login
```

3. **Deploy โปรเจกต์**
```bash
vercel
```

4. **ตั้งค่า Environment Variables บน Vercel**
ไปที่ Vercel Dashboard → Project Settings → Environment Variables แล้วเพิ่ม:
- `DJANGO_SECRET_KEY`
- `SUPABASE_DB_PASSWORD`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `DEBUG=False`

### วิธี Deploy ผ่าน GitHub Integration

1. เชื่อมต่อ GitHub repository กับ Vercel
2. ตั้งค่า Environment Variables ตามด้านบน
3. Vercel จะ auto-deploy ทุกครั้งที่ push code ใหม่

---

## 🧪 การทดสอบ

รันคำสั่งเพื่อทดสอบโปรเจกต์:

```bash
# รัน unit tests
python manage.py test

# ตรวจสอบ code style
flake8 .

# ตรวจสอบ security issues
python manage.py check --deploy
```

---

## 🐛 Troubleshooting

### ปัญหา: ติดตั้ง requirements ไม่สำเร็จ
**วิธีแก้:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --no-cache-dir
```

### ปัญหา: Database connection error
**วิธีแก้:**
- ตรวจสอบว่าไฟล์ `.env` มี `SUPABASE_DB_PASSWORD` ถูกต้อง
- ตรวจสอบ connection string ใน `settings.py`
- ตรวจสอบว่า Supabase database online อยู่

### ปัญหา: Static files ไม่โหลด
**วิธีแก้:**
```bash
python manage.py collectstatic
```

### ปัญหา: Port 8000 ถูกใช้งานแล้ว
**วิธีแก้:**
```bash
# ใช้ port อื่น
python manage.py runserver 8080
```

---

## 🤝 การมีส่วนร่วม (Contributing)

เรายินดีรับ contributions จากทุกคน! 

1. **Fork** โปรเจกต์นี้
2. **สร้าง branch** ใหม่:
   ```bash
   git checkout -b feature/ชื่อฟีเจอร์ของคุณ
   ```
3. **Commit** การเปลี่ยนแปลง:
   ```bash
   git commit -m "Add: เพิ่มฟีเจอร์ใหม่"
   ```
4. **Push** ไปยัง branch:
   ```bash
   git push origin feature/ชื่อฟีเจอร์ของคุณ
   ```
5. **สร้าง Pull Request** มาที่ repository หลัก

### แนวทางการเขียน Code
- เขียน code ให้สะอาดและอ่านง่าย
- Comment ส่วนที่ซับซ้อน
- ทดสอบ code ก่อน commit
- ใช้ชื่อ commit messages ที่มีความหมาย

---

## 👥 ทีมผู้พัฒนา

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Nomu2448">
        <img src="https://github.com/Nomu2448.png" width="100px;" alt="Nomu2448"/><br />
        <sub><b>นายนนทพัทธ์ นะทีศรี</b></sub>
      </a><br />
      <a href="https://github.com/Nomu2448">@Nomu2448</a>
    </td>
    <td align="center">
      <a href="https://github.com/bXiilzy">
        <img src="https://github.com/bXiilzy.png" width="100px;" alt="bXiilzy"/><br />
        <sub><b>นางสาวจีรนันท์ เกิดกล้า</b></sub>
      </a><br />
      <a href="https://github.com/bXiilzy">@bXiilzy</a>
    </td>
    <td align="center">
      <a href="https://github.com/Wathanyoo99">
        <img src="https://github.com/Wathanyoo99.png" width="100px;" alt="Wathanyoo99"/><br />
        <sub><b>นายวทัญญู ช่างเกวียน</b></sub>
      </a><br />
      <a href="https://github.com/Wathanyoo99">@Wathanyoo99</a>
    </td>
    <td align="center">
      <a href="https://github.com/BunnyGus">
        <img src="https://github.com/BunnyGus.png" width="100px;" alt="BunnyGus"/><br />
        <sub><b>นายนิลรักษ์ บุตรโพธิ์ศรี</b></sub>
      </a><br />
      <a href="https://github.com/BunnyGus">@BunnyGus</a>
    </td>
  </tr>
</table>

---

## 📝 License

โปรเจกต์นี้เผยแพร่ภายใต้ **MIT License** - ดูรายละเอียดใน [LICENSE](LICENSE)  
สามารถนำไปใช้ ปรับแต่ง หรือพัฒนาต่อยอดได้โดยอิสระ

---

## 📞 ติดต่อ

- 🌐 **Website:** [CodeFitKub on Vercel](https://codefitkub.vercel.app)
- 💻 **GitHub:** [github.com/Nomu2448/Codefitkub](https://github.com/Nomu2448/Codefitkub)
- 📧 **Email:** [ติดต่อผ่าน GitHub Issues](https://github.com/Nomu2448/Codefitkub/issues)

---

## 🙏 Acknowledgments

- ขอบคุณ [Django Project](https://www.djangoproject.com/) สำหรับ framework ที่ยอดเยี่ยม
- ขอบคุณ [Supabase](https://supabase.com/) สำหรับ database hosting
- ขอบคุณ [Vercel](https://vercel.com/) สำหรับ deployment platform
- ขอบคุณทุกคนที่มีส่วนร่วมในโปรเจกต์นี้

---

<p align="center">
  <strong>© 2025 — Developed with ❤️ by Team CodeFitKub</strong><br>
  <em>สุขภาพดี เริ่มต้นได้ที่นี่! 💙</em>
</p>
