FROM python:3.9.2
WORKDIR /code
COPY ./taskmanager .
COPY ./requirements.txt .
RUN pip install -r /code/requirements.txt
CMD gunicorn taskmanager.wsgi:application --bind 0.0.0.0:8000
