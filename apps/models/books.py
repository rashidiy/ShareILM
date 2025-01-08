from decimal import Decimal

from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django_resized import ResizedImageField
from apps.utils.validators import validate_file_type

from accounts.models import User
from .authors import Author
from .base import BaseModel
from .categories import Category


class Book(BaseModel):
    # Availability - kitobning mavjudlik holatlari
    class Availability(models.TextChoices):
        in_stock = 'In stock', 'In stock'  # Mavjud
        out_of_stock = 'Out of stock', 'Out of stock'  # Mavjud emas
        on_sale = 'On sale', 'On sale'  # Sotuvda
        new = 'New', 'New'  # Yangi

    # Format - kitobning formatlari
    class Format(models.TextChoices):
        standard = 'Standard', 'Standard'  # Standart
        downloadable = 'Downloadable', 'Downloadable'  # Yuklab olinadigan
        external = 'External', 'External'  # Tashqi format

    # 'title' maydoni kitob nomini saqlaydi
    title = models.CharField(max_length=250)

    # 'author' maydoni kitob muallifiga bog'lanadi
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # 'price' maydoni kitob narxini saqlaydi
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # 'category' maydoni kitobni kategoriyalarga bog'laydi
    category = models.ManyToManyField(Category, related_name='categories', blank=True)

    # 'availability' maydoni kitobning mavjudlik holatini saqlaydi
    availability = models.CharField(max_length=250, choices=Availability.choices)

    # 'format' maydoni kitobning formatini saqlaydi
    format = models.CharField(max_length=250, choices=Format.choices)

    # 'book_image' maydoni kitobning rasmini saqlaydi, o'lchamlari o'zgartiriladi
    book_image = ResizedImageField(size=[219, 317], crop=['middle', 'center'], upload_to='images/',
                                   validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp', 'webp'])],
                                   null=True, blank=True)

    # 'book_pdf' maydoni kitobning PDF formatidagi faylini saqlaydi
    book_pdf = models.FileField(upload_to='books_pdf/',
                                validators=[validate_file_type], null=True, blank=True)

    # 'owner' maydoni kitob egasiga bog'lanadi
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')

    # 'average_rating' maydoni kitobning o'rtacha reytingini saqlaydi
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)  # todo o'zgartirish

    # 'language' maydoni kitobning tilini saqlaydi
    language = models.CharField(max_length=250, null=True, blank=True)

    # 'pages' maydoni kitobdagi sahifalar sonini saqlaydi
    pages = models.PositiveIntegerField(null=True, blank=True)

    # 'description' maydoni kitobning qisqacha tavsifini saqlaydi
    description = models.TextField(null=True, blank=True)

    # 'publisher' maydoni kitobning nashriyotini saqlaydi
    publisher = models.CharField(max_length=250, null=True, blank=True)

    # 'isbn' maydoni kitobning ISBN kodini saqlaydi
    isbn = models.CharField(max_length=250)

    # 'quantity' maydoni kitobning miqdorini saqlaydi
    quantity = models.PositiveIntegerField()

    # O'rtacha reytingni yangilash uchun metod
    def update_average_rating(self):
        reviews = self.reviews.all()  # Kitobga oid barcha sharhlarni olish
        if reviews.exists():  # Agar sharhlar mavjud bo'lsa
            total_rating = sum(review.rating for review in reviews if review.rating is not None)  # Reytinglarni yig'ish
            self.average_rating = round(Decimal(total_rating) / Decimal(reviews.count()),
                                        1)  # O'rtacha reyting hisoblash
        else:
            self.average_rating = 0  # Agar sharh bo'lmasa, reyting 0 bo'ladi
        self.save()  # Ma'lumotlarni saqlash

    # Kitob nomini qaytarish uchun metod
    def __str__(self):
        return self.title

    class Meta:
        # Kitoblar tartibda eng oxirgi qo'shilganini birinchi qilish
        ordering = ['-pk']


class Review(models.Model):
    # 'book' maydoni sharh qilingan kitobga bog'lanadi
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    # 'user' maydoni sharh yozgan foydalanuvchiga bog'lanadi
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # 'text' maydoni sharh matnini saqlaydi
    text = models.TextField()

    # 'rating' maydoni sharhdagi reytingni saqlaydi, 1 dan 5 gacha bo'lishi kerak
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True)

    # 'created_at' maydoni sharh yozilgan vaqtni saqlaydi
    created_at = models.DateTimeField(auto_now_add=True)

    # Sharh ob'ekti matnini qaytarish
    def __str__(self):
        return f"{self.user}-{self.book}"
