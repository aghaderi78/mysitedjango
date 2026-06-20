# Django Polls — رسمی‌ترین خروجی تمرین Tutorial 01 تا 08

این پروژه دقیقاً بر اساس آخرین نسخه‌ی مستندات رسمی جنگو (Django 6.0) ساخته شده:
https://docs.djangoproject.com/en/6.0/intro/tutorial01/ تا
https://docs.djangoproject.com/en/6.0/intro/tutorial08/

همه‌ی کدها تست شده و به‌صورت کامل اجرا می‌شوند (مدل‌ها، migration، تمپلیت‌ها،
استاتیک فایل‌ها، پنل ادمین سفارشی‌شده، و ۱۰ تست خودکار).

## چی توشه؟

- **Tutorial 1** — پروژه `mysite` + اپ `polls` + اولین view و URLconf
- **Tutorial 2** — مدل‌های `Question` و `Choice`، migration، و پنل ادمین پیش‌فرض
- **Tutorial 3** — view های واقعی، تمپلیت‌ها، `get_object_or_404`، namespace کردن URL ها (`polls:`)
- **Tutorial 4** — فرم رای‌گیری (`vote`)، و تبدیل view ها به Generic Views (`ListView`/`DetailView`)
- **Tutorial 5** — ۱۰ تست خودکار در `polls/tests.py` (مدل + ایندکس + دیتیل)
- **Tutorial 6** — استایل CSS و بک‌گراند ایمیج به‌عنوان static files
- **Tutorial 7** — سفارشی‌سازی کامل پنل ادمین (fieldsets، inline choices، list_display،
  list_filter، search_fields) و سفارشی‌سازی تمپلیت `admin/base_site.html`
- **Tutorial 8** — توضیح و راهنمای نصب `django-debug-toolbar` (در `requirements.txt` کامنت شده)

## اجرا (Run)

```bash
# 1) ساخت محیط مجازی (اختیاری ولی پیشنهادی)
python3 -m venv venv
source venv/bin/activate        # ویندوز: venv\Scripts\activate

# 2) نصب وابستگی‌ها
pip install -r requirements.txt

# 3) اجرای migration ها
python manage.py migrate

# 4) ساخت یوزر ادمین
python manage.py createsuperuser

# 5) اجرای تست‌ها (باید ۱۰ تست پاس شود)
python manage.py test polls

# 6) اجرای سرور توسعه
python manage.py runserver
```

سپس در مرورگر:

- صفحه‌ی اصلی نظرسنجی‌ها: http://127.0.0.1:8000/polls/
- پنل ادمین: http://127.0.0.1:8000/admin/

> هیچ سؤالی در دیتابیس نیست؛ بعد از لاگین در ادمین یک «Question» و چند «Choice»
> اضافه کنید تا صفحه‌ی polls چیزی نشان دهد.

## فعال کردن Django Debug Toolbar (Tutorial 8 — اختیاری)

۱. خط `django-debug-toolbar` را در `requirements.txt` از کامنت خارج کنید و دوباره نصب کنید:
   ```bash
   pip install django-debug-toolbar
   ```
۲. مطابق راهنمای رسمی پکیج این موارد را اضافه کنید:
   https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
   - افزودن `"debug_toolbar"` به `INSTALLED_APPS` در `mysite/settings.py`
   - افزودن میدل‌ور `"debug_toolbar.middleware.DebugToolbarMiddleware"` به `MIDDLEWARE`
   - افزودن `INTERNAL_IPS = ["127.0.0.1"]` در `settings.py`
   - افزودن مسیر toolbar در `mysite/urls.py`:
     ```python
     from django.conf import settings

     if settings.DEBUG:
         import debug_toolbar
         urlpatterns = [
             path("__debug__/", include(debug_toolbar.urls)),
         ] + urlpatterns
     ```
این مرحله را عمداً به‌صورت پیش‌فرض فعال نکرده‌ام چون به محیط اجرای شما (لوکال،
داکر، و غیره) بستگی دارد و ممکنه `INTERNAL_IPS` نیاز به مقدار متفاوتی داشته باشد.

## ساختار پروژه

```
djangotutorial/
├── manage.py
├── requirements.txt
├── mysite/                  # تنظیمات پروژه
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── polls/                   # اپ نظرسنجی
│   ├── models.py
│   ├── views.py             # Generic Views (ListView / DetailView) + vote
│   ├── urls.py
│   ├── admin.py             # پنل ادمین سفارشی‌شده
│   ├── tests.py             # ۱۰ تست خودکار
│   ├── migrations/
│   ├── templates/polls/
│   └── static/polls/
└── templates/admin/         # تمپلیت ادمین سفارشی‌شده (سراسر پروژه)
```
