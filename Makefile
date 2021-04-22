APP_NAME = morphey

run:
	@docker-compose up

build:
	@docker-compose build

stop:
	@docker-compose stop

bash:
	@docker exec -it $(APP_NAME) bash

# Create migrations: make migrations name="add_user"
migrations:
	@docker-compose run $(APP_NAME) alembic revision --autogenerate -m "${name}"

migrate:
	@docker-compose un $(APP_NAME) alembic upgrade head

clean: stop
	@docker-compose down --remove-orphans -v

# Testing
test:
	@docker-compose -f $(dev_docker_compose) run $(APP_NAME) pytest tests --verbose -vv -s -W ignore::DeprecationWarning -k "${name}"

cov:
	@docker-compose -f $(dev_docker_compose) run $(APP_NAME)
