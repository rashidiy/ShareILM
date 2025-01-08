from django.db import models

from .base import BaseModel


class OrderItem(BaseModel):
    # OrderStatus - buyurtma holatlari
    class OrderStatus(models.TextChoices):
        new = 'New', 'New'  # Yangi buyurtma
        sent = 'Sent', 'Sent'  # Yuborilgan
        canceled = 'Canceled', 'Canceled'  # Bekor qilingan

    # 'book' maydoni buyurtma qilinayotgan kitobni saqlaydi, har bir kitob faqat bitta buyurtmada bo'lishi mumkin
    book = models.OneToOneField('apps.Book', on_delete=models.CASCADE, related_name='book_orders')

    # 'order_status' maydoni buyurtmaning holatini saqlaydi
    order_status = models.CharField(max_length=250, choices=OrderStatus.choices, default=OrderStatus.new)

    # 'quantity' maydoni buyurtma qilinayotgan kitobning miqdorini saqlaydi
    quantity = models.PositiveIntegerField(default=1)

    # Buyurtma ob'ekti matnini qaytarish
    def __str__(self):
        return f"{self.quantity}-{self.book}"


class Cart(BaseModel):
    # CartStatus - savatning holatlari
    class CartStatus(models.TextChoices):
        saved = 'Saved', 'Saved'  # Saqlangan
        sent = 'Sent', 'Sent'  # Yuborilgan
        canceled = 'Canceled', 'Canceled'  # Bekor qilingan

    # 'user' maydoni savatni yaratgan foydalanuvchiga bog'lanadi
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='carts')

    # 'orders' maydoni savatdagi buyurtmalarni saqlaydi, har bir savatda bir nechta buyurtmalar bo'lishi mumkin
    orders = models.ManyToManyField(OrderItem, related_name='carts', blank=True)

    # 'cart_status' maydoni savatning holatini saqlaydi
    cart_status = models.CharField(max_length=250, choices=CartStatus.choices, default=CartStatus.saved)

    # Savat ob'ekti matnini qaytarish
    def __str__(self):
        return f"Cart_id:{self.id} - {self.user.username}"
