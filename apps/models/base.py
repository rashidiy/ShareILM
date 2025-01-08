from django.db import models


class BaseModel(models.Model):
    # 'created_at' maydoni model yaratilib, saqlanganda avtomatik tarzda hozirgi sana va vaqtni saqlaydi
    created_at = models.DateTimeField(auto_now_add=True)

    # 'updated_at' maydoni har safar model yangilanganida avtomatik ravishda hozirgi sana va vaqtni saqlaydi
    updated_at = models.DateTimeField(auto_now=True)

    # Bu modelni faqat boshqa modellarda meros olish uchun ishlatish mumkin. O'zi to'g'ridan-to'g'ri bazaga saqlanmaydi.
    class Meta:
        abstract = True
