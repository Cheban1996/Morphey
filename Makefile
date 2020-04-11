APP_NAME = morphey

run:
	PYTHONPATH="$(PWD)"
	PYTHONASYNCIODEBUG=1
	python morphey/app.py

run-ws:
	PYTHONASYNCIODEBUG=1
	python morphey/ws-demon.py

run-worker-jobs:
	arq morphey/worker-jobs.WorkerSettings

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

test:
	pytest tests --verbose -s -vv --disable-warnings -k "${k}"

ui-run:
	npm run --prefix ui-morphey/ serve

ui-build:
	rm -rf ui-morphey/dist
	npm run --prefix ui-morphey/ build
	http-server ui-morphey/dist/
