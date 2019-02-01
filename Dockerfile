FROM python:3.5.6-slim

EXPOSE 8000

RUN mkdir -p /var/app
WORKDIR /var/app

# Install Dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends default-libmysqlclient-dev unzip gcc git apache2 python3-dev libapache2-mod-wsgi-py3 libsasl2-dev libldap2-dev libssl-dev libcurl4-openssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*


ADD requirements.txt /var/app
RUN pip install -r requirements.txt

ADD . .

CMD python manage.py runserver 0.0.0.0:8000
