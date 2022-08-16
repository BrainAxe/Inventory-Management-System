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

test:
	docker exec -it inventory-web python manage.py test

createsuperuser:
	docker exec -it inventory-web python manage.py createsuperuser

.PHONEY: build up down start stop makemigrations migrate test createsuperuser
