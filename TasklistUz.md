# ShareILM Vazifa Boshqaruvchisi

## Bo'limlar

<details>
<summary>1.Loyihani sozlash</summary>

- [ ] 1.ShareILM repozitoriyasini fork qilib, lokalga yuklab oling.
- [ ] 2.Virtual muhitni `venv` yoki `pipenv` yordamida sozlang.
- [ ] 3.`requirements.txt` faylida keltirilgan barcha bog'liqliklarni o'rnating.
- [ ] 4.`.env` faylini yarating va ma'lumotlar bazasi sozlamalarini konfiguratsiya qiling.
- [ ] 5.Dastlabki migratsiyalarni ishga tushiring va ma'lumotlar bazasi ulanishini tekshiring.
- [ ] 6.`python manage.py runserver` buyrug'i yordamida serverni ishga tushiring.
- [ ] 7.README faylida "Lokal sozlash" bo'limini qo'shib, sozlash jarayonini hujjatlashtiring.
- [ ] 8.`django-environ` kutubxonasidan foydalangan holda xavfsiz muhit sozlamalarini boshqaring.
- [ ] 9.Superuser yarating va administrator sifatida tizimga kiring.
- [ ] 10.Statik va media fayllar uchun lokal sozlamalarni konfiguratsiya qiling.

</details>

<details>
<summary>2.Modellar</summary>

- [ ] 11.Mavjud modellarni ko'rib chiqing va har bir maydon uchun izohlar yozing.
- [ ] 12.`Book` modelini yarating: `title`, `author`, `publisher`, `ISBN`, `price`, `stock`, `category`, va `cover_image` maydonlari bilan.
- [ ] 13.`Category` modelini yarating: `name`, `slug`, va `description` maydonlari bilan.
- [ ] 14.`Book` modeliga `Category` modeliga foreign key qo'shing.
- [ ] 15.`Borrower` modelini yarating: `user`, `borrowed_books`, `due_date`, va `return_status` maydonlari bilan.
- [ ] 16.Kitob zaxirasini tekshirish uchun `Book` modelida maxsus metodlarni qo'shing.
- [ ] 17.Kitob sotib olish va qarz olish jarayonlarini qayd etish uchun `Transaction` modelini amalga oshiring.
- [ ] 18.Yangi modellar uchun migratsiya skriptini yozing.
- [ ] 19.Barcha maxsus model metodlari uchun unit-testlar qo'shing.
- [ ] 20.Modellarni Django shell yordamida sinab ko'ring.
- [ ] 21.`faker` yordamida `Book` va `Category` modellarini namunaviy ma'lumotlar bilan to'ldiruvchi maxsus Django komandasi yarating.
- [ ] 22.`Book` va `Category` modellar uchun namuna ma'lumotlarini avvaldan yuklash uchun fixtures qo'shing.

</details>

<details>
<summary>3.Ko'rinishlar va URL manzillar</summary>

- [ ] 23.Barcha kitoblarni sahifalash bilan ko'rsatish uchun ko'rinish yarating.
- [ ] 24.Har bir kitob uchun batafsil ma'lumot sahifasini yarating.
- [ ] 25.Kitoblarni sarlavha, muallif yoki ISBN bo'yicha qidirish funksiyasini amalga oshiring.
- [ ] 26.Kategoriyalar bo'yicha kitoblarni ko'rsatish uchun ko'rinish yarating.
- [ ] 27.Kitoblarga tegishli barcha ko'rinishlar uchun URL manzillarni yozing.
- [ ] 28.Foydalanuvchi tajribasini yaxshilash uchun nonushta navigatsiyasini amalga oshiring.
- [ ] 29.Foydalanuvchilar uchun kitoblarni qarz olish va qarz holatini kuzatish uchun ko'rinish yarating.
- [ ] 30.Administratorlar uchun zaxira darajasini boshqarish uchun boshqaruv paneli yarating.
- [ ] 31.Ko'rinishlarda so'rovlarni samaradorlik uchun optimallashtiring.

</details>

<details>
<summary>4.Shablonlar</summary>

- [ ] 32.Bosh shablonni bir xil header, footer va sidebar bilan yarating.
- [ ] 33.Yaqinda qo'shilgan va tavsiya etilgan kitoblarni ko'rsatadigan bosh sahifa shablonini yarating.
- [ ] 34.Kitob ma'lumotlari va zaxira holatini ko'rsatadigan kitob tafsiloti shablonini qo'shing.
- [ ] 35.Kitoblar uchun qidiruv natijalari shablonini yarating.
- [ ] 36.Kategoriyalarni rasmlar bilan ko'rsatadigan shablonni amalga oshiring.
- [ ] 37.Kitob narxlarini formatlash uchun maxsus shablon filtrini yozing.
- [ ] 38."Mening qarzga olingan kitoblarim" sahifasi uchun moslashuvchan shablon yarating.
- [ ] 39.Shablonlarni mobil va ish stollari qurilmalarida sinab ko'ring.

</details>

<details>
<summary>5.Testlash</summary>

- [ ] 40.Lokal sozlamalar to'g'ri ishlashini ta'minlash uchun skriptlarni sinovdan o'tkazing.
- [ ] 41.Barcha maxsus model metodlari uchun unit-testlar qo'shing.
- [ ] 42.Kitoblarga tegishli ko'rinishlar uchun integratsiya testlari yarating.
- [ ] 43.Shablonlarning har xil qurilmalarda javob qaytarishini sinab ko'ring.
- [ ] 44.Yangilanishlar uchun regressiya testlarini avtomatlashtiring.

</details>

<details>
<summary>6.Docker</summary>

- [ ] 45.`docker-compose.yml` faylini PostgreSQL bilan lokal rivojlantirish uchun qo'shing.
- [ ] 46.`docker-compose up` buyrug'ini ishga tushirib, Docker sozlamasini sinab ko'ring.
- [ ] 47.Docker sozlash jarayonini hujjatlashtiring.
- [ ] 48.Muhim xizmatlar uchun Docker sog'liqni tekshirishlarini yozing.
- [ ] 49.Dockerfile ni tezroq qurilish uchun optimallashtiring.

</details>
