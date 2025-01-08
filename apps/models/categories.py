from django.db import models


class Category(models.Model):
    # 'name' maydoni kategoriya nomini saqlaydi, maksimal uzunligi 100 ta belgidan iborat
    name = models.CharField(max_length=100)

    # 'description' maydoni kategoriya haqida qisqacha tavsifni saqlaydi; bu maydon ixtiyoriy va bo‘sh yoki null bo‘lishi mumkin
    description = models.TextField(null=True, blank=True)

    # 'name' maydonini qaytaradi, ob'ektning matnli tasvirini beradi
    def __str__(self):
        return self.name
