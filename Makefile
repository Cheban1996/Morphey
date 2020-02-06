APP_NAME = morphey

run:
	PYTHONASYNCIODEBUG=1 python app.py

run-ws:
	PYTHONASYNCIODEBUG=1 python ws-demon.py

build:
	@docker-compose build

build-ws-demon:
	@docker-compose build ws-demon  # docker build -t ws-demon -f ws-demon.Dockerfile .

build-morphey:
	@docker-compose build morphey  # docker build -t morphey -f morphey.Dockerfile .

up:
	@docker-compose up -d

up-ws-demon:
	@docker-compose up ws-demon

up-morphey:
	@docker-compose up morphey

up-redis:
	@docker-compose up redis

stop:
	@docker-compose stop