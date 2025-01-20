# ShareILM loyihasini lokal sozlash va ishga tushirish bo‘yicha qo‘llanma

Quyida ShareILM loyihasini lokal muhitda sozlash va ishga tushirish bo‘yicha batafsil ko‘rsatmalar berilgan:

---

### **1. Repozitoriyani fork qilish va lokalga yuklash**

1. GitHub’da ShareILM repozitoriyasini **Fork** qiling.  
2. Fork qilingan repozitoriyani lokal muhitga yuklash uchun quyidagi buyruqni ishlating:  
   ```bash
   git clone https://github.com/username/ShareILM.git
   cd ShareILM
   ```

---

### **2. Virtual muhit (venv) yaratish va faollashtirish**

Python virtual muhitini yaratish va faollashtirish uchun quyidagi buyruqlarni bajaring:

```bash
# Virtual muhitni yaratish
python -m venv .venv

# Virtual muhitni faollashtirish (Windows)
.venv\Scripts\activate

# Virtual muhitni faollashtirish (Linux/MacOS)
source .venv/bin/activate
```

---

### **3. Kerakli paketlarni o‘rnatish**

`requirement.txt` faylidagi barcha zaruriy kutubxonalarni o‘rnatish uchun quyidagi buyruqni bajaring:

```bash
pip install -r requirements.txt
```

---

### **4. Redis serverni ishga tushirish**

Loyihaning Redis bilan bog‘liq qismlari ishlashi uchun Redis serverni ishga tushirish kerak. Buning uchun Docker’dan foydalanishingiz mumkin:

#### **Docker orqali Redis serverni ishga tushirish:**
```bash
docker run --name redis-server -p 6379:6379 -d redis
```

Agar kompyuteringizda Docker o‘rnatilmagan bo‘lsa yoki Redis’ni Docker orqali ishlatishni xohlamasangiz, alternativ usul sifatida Redis serverni [rasmiy Redis saytidan](https://redis.io/download) yuklab olib, lokal muhitda ishga tushirishingiz mumkin.

---

### **5. Migratsiyalarni bajarish**

Loyihada ishlatiladigan ma’lumotlar bazasini yaratish uchun quyidagi buyruqlarni ketma-ket bajaring:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **6. Superuser yaratish**

Admin panelga kirish uchun superuser yaratishingiz kerak. Buning uchun quyidagi buyruqni bajaring va so‘ralgan ma’lumotlarni to‘ldiring:

```bash
python manage.py createsuperuser
```

---

### **7. `.env` faylini sozlash**

Loyihada ishlatiladigan muhit o‘zgaruvchilarini sozlash uchun `.env` faylini yaratib, `.env.example` faylidagi o‘zgaruvchilarni nusxa ko‘chirib oling. So‘ng, o‘z konfiguratsiyalaringizni kiriting:

```ini
SECRET_KEY=your_secret_key
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
```

---

### **8. Loyihani ishga tushirish**

Loyihani lokal muhitda ishga tushirish uchun quyidagi buyruqni bajaring:

```bash
python manage.py runserver
```

Brauzeringizda quyidagi manzilga kirib, loyihaning ishlayotganligini tekshirishingiz mumkin:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

### **Qo‘shimcha eslatmalar**

- Agar Redis server yoki boshqa xizmatlar bilan bog‘liq muammolar yuzaga kelsa, Docker konteynerni qayta ishga tushirishingiz mumkin:  
  ```bash
  docker restart redis-server
  ```
- `.env` faylingizni hech qachon ommaga oshkor qilmang, chunki u muhim maxfiy ma’lumotlarni o‘z ichiga oladi.

---

Loyiha bo‘yicha savollar yoki muammolar yuzaga kelsa, muhokama yoki PR (Pull Request) orqali bog‘lanishingiz mumkin.
