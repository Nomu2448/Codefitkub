const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');
const session = require('express-session');
const bodyParser = require('body-parser');
const path = require('path');

const app = express();
const PORT = 3000;

// เชื่อมต่อฐานข้อมูล SQLite
const db = new sqlite3.Database('./users.db', (err) => {
  if (err) {
    console.error('เกิดข้อผิดพลาดในการเชื่อมต่อฐานข้อมูล:', err);
  } else {
    console.log('เชื่อมต่อฐานข้อมูล SQLite สำเร็จ');
  }
});

// สร้างตารางผู้ใช้
db.run(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT,
    bio TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
  )
`);

// Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));
app.use(session({
  secret: 'your-secret-key-change-this',
  resave: false,
  saveUninitialized: false,
  cookie: { secure: false } // ตั้งเป็น true ถ้าใช้ HTTPS
}));

// Middleware ตรวจสอบการล็อกอิน
function isAuthenticated(req, res, next) {
  if (req.session.userId) {
    return next();
  }
  res.status(401).json({ error: 'กรุณาเข้าสู่ระบบ' });
}

// Routes

// 1. สมัครสมาชิก
app.post('/api/register', async (req, res) => {
  const { username, password, email } = req.body;

  if (!username || !password) {
    return res.status(400).json({ error: 'กรุณากรอก username และ password' });
  }

  try {
    const hashedPassword = await bcrypt.hash(password, 10);
    
    db.run(
      'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
      [username, hashedPassword, email],
      function(err) {
        if (err) {
          if (err.message.includes('UNIQUE')) {
            return res.status(400).json({ error: 'username นี้มีผู้ใช้แล้ว' });
          }
          return res.status(500).json({ error: 'เกิดข้อผิดพลาด' });
        }
        res.json({ message: 'สมัครสมาชิกสำเร็จ', userId: this.lastID });
      }
    );
  } catch (error) {
    res.status(500).json({ error: 'เกิดข้อผิดพลาดในการเข้ารหัส' });
  }
});

// 2. เข้าสู่ระบบ
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  db.get('SELECT * FROM users WHERE username = ?', [username], async (err, user) => {
    if (err) {
      return res.status(500).json({ error: 'เกิดข้อผิดพลาด' });
    }

    if (!user) {
      return res.status(400).json({ error: 'username หรือ password ไม่ถูกต้อง' });
    }

    const match = await bcrypt.compare(password, user.password);
    
    if (!match) {
      return res.status(400).json({ error: 'username หรือ password ไม่ถูกต้อง' });
    }

    req.session.userId = user.id;
    req.session.username = user.username;
    
    res.json({ 
      message: 'เข้าสู่ระบบสำเร็จ',
      user: {
        id: user.id,
        username: user.username,
        email: user.email
      }
    });
  });
});

// 3. ออกจากระบบ
app.post('/api/logout', (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({ error: 'เกิดข้อผิดพลาด' });
    }
    res.json({ message: 'ออกจากระบบสำเร็จ' });
  });
});

// 4. ดึงข้อมูล Profile
app.get('/api/profile', isAuthenticated, (req, res) => {
  db.get('SELECT id, username, email, bio, created_at FROM users WHERE id = ?', 
    [req.session.userId], 
    (err, user) => {
      if (err) {
        return res.status(500).json({ error: 'เกิดข้อผิดพลาด' });
      }
      res.json(user);
    }
  );
});

// 5. อัพเดต Profile
app.put('/api/profile', isAuthenticated, (req, res) => {
  const { email, bio } = req.body;

  db.run(
    'UPDATE users SET email = ?, bio = ? WHERE id = ?',
    [email, bio, req.session.userId],
    function(err) {
      if (err) {
        return res.status(500).json({ error: 'เกิดข้อผิดพลาด' });
      }
      res.json({ message: 'อัพเดตข้อมูลสำเร็จ' });
    }
  );
});

// 6. ตรวจสอบสถานะการล็อกอิน
app.get('/api/check-auth', (req, res) => {
  if (req.session.userId) {
    res.json({ 
      authenticated: true, 
      username: req.session.username 
    });
  } else {
    res.json({ authenticated: false });
  }
});

// เริ่มเซิร์ฟเวอร์
app.listen(PORT, () => {
  console.log(`Server กำลังทำงานที่ http://localhost:${PORT}`);
});