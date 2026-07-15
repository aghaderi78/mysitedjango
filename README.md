# mysitedjango

یک پروژه‌ی Django شامل اپ نظرسنجی (Polls) که کاربران می‌توانند سوالات را ببینند و رأی بدهند.

## 📋 امکانات

- نمایش لیست سوالات نظرسنجی
- رأی‌گیری روی گزینه‌ها
- نمایش نتایج
- پنل ادمین جنگو

## 🛠 تکنولوژی‌ها

- Python / Django
- SQLite

## 📁 ساختار پروژه

```
djangotutorial/
├── manage.py
├── requirements.txt
├── mysite/       # تنظیمات اصلی پروژه
└── polls/        # اپ نظرسنجی
```

## ⚙️ نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.x
- pip

### مراحل نصب

۱. کلون کردن ریپازیتوری:
```bash
git clone https://github.com/aghaderi78/mysitedjango.git
cd mysitedjango/djangotutorial
```

۲. ساخت و فعال‌سازی محیط مجازی:
```bash
python -m venv venv
source venv/bin/activate      # در لینوکس/مک
venv\Scripts\activate         # در ویندوز
```

۳. نصب وابستگی‌ها:
```bash
pip install -r requirements.txt
```

۴. اجرای مایگریشن‌های دیتابیس:
```bash
python manage.py migrate
```

۵. (اختیاری) ساخت یوزر ادمین برای دسترسی به پنل مدیریت:
```bash
python manage.py createsuperuser
```

۶. اجرای سرور توسعه:
```bash
python manage.py runserver
```

سپس در مرورگر به آدرس زیر بروید:
```
http://127.0.0.1:8000/
```

برای دسترسی به پنل ادمین:
```
http://127.0.0.1:8000/admin/
```

## 👤 نویسنده

**Alireza Ghaderi**
[GitHub](https://github.com/aghaderi78)
