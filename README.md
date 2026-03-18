# 🚀 Safobek Portfolio — Django + Glassmorphism

Personal portfolio sayt. Python Django backend, HTML/CSS/JS Glassmorphism frontend.

---

## 📁 Papka strukturasi

```
safobek_portfolio/
├── config/              # Django konfiguratsiya
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                # Asosiy app
│   ├── models.py        # Profile, Experience, SocialLink, ContactInfo
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── templates/
│   └── main/
│       └── index.html   # Glassmorphism frontend
├── static/
│   ├── css/style.css    # Barcha stillar
│   └── js/main.js       # Tab tizimi JS
├── media/               # Yuklangan rasmlar
├── db.sqlite3           # SQLite bazasi
├── manage.py
└── requirements.txt
```

---

## ⚙️ O'rnatish va ishga tushirish

### 1. Muhit tayyorlash

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
```

### 2. Migratsiyalar

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Superuser yaratish (Admin uchun)

```bash
python manage.py createsuperuser
# Username, email, parol kiriting
```

### 4. Serverni ishga tushirish

```bash
python manage.py runserver
```

Sayt: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin

---

## 🔧 Admin paneldan boshqarish

Admin panelga kiring: http://127.0.0.1:8000/admin

### Modellar:

| Model | Nima uchun |
|-------|-----------|
| **Profile** | Ism, rasm, bio, tajriba yillari, loyihalar soni, "Birga ishlash" URL |
| **Experience** | Ish tajribasi timeline (yil, sarlavha, tavsif) |
| **SocialLink** | Instagram, Telegram, GitHub va boshqa tarmoqlar |
| **ContactInfo** | Manzil, telefon, email |

---

## 🎨 Dizayn

- **Uslub**: Glassmorphism (shisha effekti)
- **Shrift**: Sora + JetBrains Mono
- **Tablar**: Haqida / Tajriba / Tarmoqlar / Aloqa
- **Animatsiyalar**: Orb floats, avatar ring spin, card entrance, timeline stagger

---

## 📦 requirements.txt

```
Django>=4.2
Pillow>=10.0
```

---

## 🌐 Production uchun (safobek.uz)

```python
# settings.py da o'zgartiring:
DEBUG = False
ALLOWED_HOSTS = ['safobek.uz', 'www.safobek.uz']
SECRET_KEY = 'yangi-maxfiy-kalit'  # Yangi kalit yarating!
```

```bash
python manage.py collectstatic
```

---

## 💡 "Birga ishlash" tugmasini sozlash

Admin panel → Profile → `work_together_url` maydoniga:
- Telegram: `https://t.me/username`
- Email: `mailto:sizning@email.com`

---

*Loyiha MuhammadSafo Abduqaxxorov uchun yaratildi.*
