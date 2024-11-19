install: 
	poetry install

migrations: 
	poetry run python manage.py makemigrations

migrate: 
	poetry run python manage.py migrate

superuser: 
	poetry run python manage.py createsuperuser

run:
	poetry run python manage.py runserver
