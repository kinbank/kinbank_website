# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.12-bookworm

# Install Source scripts
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/website
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN ls -l

COPY ./requirements.txt website/deploy/gunicorn_starter.sh /opt/app/
COPY website /opt/app/website/
WORKDIR /opt/app/website
RUN pip install -r /opt/app/requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# Get the data from github
RUN git clone https://github.com/kinbank/kinbank.git /opt/app/website/kinbank
RUN cd /opt/app/website/kinbank && git pull

# Add necessary data
RUN python /opt/app/website/add_columnGlottocode.py 

# Build SQL site
RUN csvs-to-sqlite /opt/app/website/kinbank/kinbank/cldf/*.csv /opt/app/website/kinbank.sqlite3
RUN csvs-to-sqlite  /opt/app/website/static/about.csv /opt/app/website/kinbank.sqlite3
RUN csvs-to-sqlite  /opt/app/website/static/website_parameters.csv /opt/app/website/kinbank.sqlite3
RUN python /opt/app/website/manage.py makemigrations
RUN python /opt/app/website/manage.py migrate

# run gunicorn
EXPOSE $PORT
ENTRYPOINT ["/opt/app/website/deploy/gunicorn_starter.sh"]

#EXPOSE 8020
#ENTRYPOINT ["/opt/app/gunicorn_starter.sh"]
