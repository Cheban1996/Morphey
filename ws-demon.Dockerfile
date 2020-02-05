FROM python:3.8

WORKDIR /wd

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "ws-demon.py" ]