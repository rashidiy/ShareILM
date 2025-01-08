from django.db import models

from .base import BaseModel


class OrderItem(BaseModel):
    class OrderStatus(models.TextChoices):
        new = 'New', 'New'
        sent = 'Sent', 'Sent'
        canceled = 'Canceled', 'Canceled'

    book = models.OneToOneField('apps.Book', on_delete=models.CASCADE, related_name='book_orders')
    order_status = models.CharField(max_length=250, choices=OrderStatus.choices, default=OrderStatus.new)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity}-{self.book}"



