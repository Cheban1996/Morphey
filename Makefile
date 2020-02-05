run:
	PYTHONASYNCIODEBUG=1 python app.py

run-ws:
	PYTHONASYNCIODEBUG=1 python ws-demon.py


build-ws-demon:
	@docker build -t ws-demon .

build-app:
	@docker build -t morphey .