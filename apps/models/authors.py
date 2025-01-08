from django.db import models


class Author(models.Model):
    # 'name' maydoni muallifning ism-sharifini saqlaydi, maksimal uzunligi 100 ta belgidan iborat
    name = models.CharField(max_length=100)

    # 'bio' maydoni muallifning qisqacha tarjimai holini yoki tasvirini saqlaydi; bu maydon ixtiyoriy va bo‘sh yoki null bo‘lishi mumkin
    bio = models.TextField(null=True, blank=True)

    # __str__ metodida muallifning ismi qaytariladi, bu ob'ektning matnli tasviridir
    def __str__(self):
        return self.name
