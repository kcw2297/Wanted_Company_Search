FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get -y upgrade
RUN pip install --upgrade pip

WORKDIR /app    
COPY . /app
RUN pip install -r requirements.txt

RUN python manage.py migrate --settings=config.settings.deploy
RUN python manage.py collectstatic --settings=config.settings.deploy

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi.deploy:application"]
