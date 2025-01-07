mig:
	python manage.py makemigrations
	python manage.py migrate

admin:
	python manage.py createsuperuser  --email admin@example.com

initial_mig:
    python manage.py dumpdata --format=json apps.category > fixtures/categories.json
    python manage.py loaddata fixtures/categories.json