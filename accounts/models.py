from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

# Foydalanuvchilarni boshqarish uchun maxsus manager sinfi
class CUserManager(UserManager):
    use_in_migrations = True  # Ushbu manager migratsiyalarda ishlatilishi mumkinligini bildiradi

    # Foydalanuvchini yaratish va saqlash uchun xususiy metod
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Berilgan email bo'sh bo'lmasligi kerak")  # Email majburiy
        user = self.model(email=email, username=username, **extra_fields)  # Modelni yaratadi
        user.password = make_password(password)  # Parolni xeshlash
        user.save(using=self._db)  # Ma'lumotlar bazasida saqlash
        return user

    # Oddiy foydalanuvchi yaratish uchun metod
    def create_user(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)  # Oddiy foydalanuvchi admin bo'lmaydi
        extra_fields.setdefault("is_superuser", False)  # Oddiy foydalanuvchi superuser bo'lmaydi
        return self._create_user(email, username, password, **extra_fields)

    # Superuser (admin) yaratish uchun metod
    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)  # Superuser admin bo'ladi
        extra_fields.setdefault("is_superuser", True)  # Superuser maxsus huquqlarga ega bo'ladi

        # Superuserda is_staff va is_superuser True bo'lishi shart
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuserda is_staff=True bo'lishi kerak.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuserda is_superuser=True bo'lishi kerak.")

        return self._create_user(email, username, password, **extra_fields)

    # Berilgan ruxsatga ega foydalanuvchilarni qaytaruvchi metod
    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:  # Agar backend berilmagan bo'lsa
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "Bir nechta autentifikatsiya backendlari mavjud, `backend` argumentini berishingiz kerak."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend satr ko'rinishidagi import yo'l bo'lishi kerak (berilgan: %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)  # Berilgan backendni yuklash
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()  # Agar backendda with_perm bo'lmasa, hech narsa qaytarilmaydi

# Foydalanuvchi modeli
class User(AbstractUser):
    USERNAME_FIELD = 'email'  # Email tizimga kirishda asosiy maydon sifatida ishlatiladi
    email = models.EmailField('Email', unique=True)  # Takrorlanmas email maydoni
    is_email_verified = models.BooleanField(default=False)  # Email tasdiqlanganligini ko'rsatadigan bayroq

    username_validator = UnicodeUsernameValidator()  # Foydalanuvchi nomini tekshiruvchi validator

    # Foydalanuvchi nomi maydoni
    username = models.CharField(
        _("username"),
        max_length=150,  # Maksimal uzunlik 150 ta belgidan oshmasligi kerak
        unique=True,  # Foydalanuvchi nomi takrorlanmas bo'lishi kerak
        help_text=_(
            "Majburiy. Maksimal 150 ta belgi. Harflar, raqamlar va @/./+/-/_ belgilariga ruxsat beriladi."
        ),
        validators=[username_validator],  # Validator yordamida tekshiriladi
        error_messages={
            "unique": _("Бундай фойдаланувчи номи аллакачон мавжуд."
            ),
        },
        null=True,  # Bo'sh qoldirilishi mumkin
        blank=True  # Formada to'ldirilmasa bo'ladi
    )

    REQUIRED_FIELDS = []  # Superuser yaratishda qo'shimcha maydonlar talab qilinmaydi

    objects = CUserManager()  # Maxsus managerni belgilash
