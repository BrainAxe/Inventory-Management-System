build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

start:
	docker-compose start

stop:
	docker-compose stop

makemigrations:
	docker exec -it inventory-web python manage.py makemigrations

migrate:
	docker exec -it inventory-web python manage.py migrate

createsuperuser:
	docker exec -it inventory-web python manage.py createsuperuser

.PHONEY: build up down start stop makemigrations migrate createsuperuser
