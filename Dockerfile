# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.7-buster


# Install NGINX
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Install Source scripts
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/website


COPY requirements.txt start-server.sh /opt/app/
COPY website /opt/app/website/
WORKDIR /opt/app/website
RUN pip install -r /opt/app/requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# Build Kinbank database
RUN git clone https://github.com/kinbank/kinbank.git /opt/app/website/kinbank
RUN python /opt/app/website/add_columnGlottocode.py 
RUN csvs-to-sqlite /opt/app/website/kinbank/kinbank/cldf/*.csv /opt/app/website/kinbank.sqlite3
RUN csvs-to-sqlite  /opt/app/website/kb/static/about.csv /opt/app/website/kinbank.sqlite3
RUN python opt/app/website/manage.py makemigrations
RUN python opt/app/website/manage.py migrate

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]


