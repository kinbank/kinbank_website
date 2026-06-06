# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.12-bookworm

SHELL ["/bin/bash", "-c"]

# Install Source scripts
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/website

COPY requirements.txt website/deploy/gunicorn_starter.sh /opt/app/

COPY website /opt/app/website/
WORKDIR /opt/app/website
RUN pip install -r /opt/app/requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# Get the data from github
RUN git clone https://github.com/kinbank/kinbank.git /opt/app/website/kinbank
RUN cd /opt/app/website/kinbank && git pull

# Add necessary data
RUN python /opt/app/website/scripts/add_columnGlottocode.py --forms-path /opt/app/website/kinbank/kinbank/cldf/forms.csv

# Strip UTF-8 BOM from languages.csv so the ID column loads correctly into SQLite
RUN python -c "p='/opt/app/website/kinbank/kinbank/cldf/languages.csv'; open(p,'w',encoding='utf-8').write(open(p,encoding='utf-8-sig').read())"

# Build SQL site
RUN csvs-to-sqlite /opt/app/website/kinbank/kinbank/cldf/*.csv /opt/app/website/kinbank.sqlite3
RUN csvs-to-sqlite  /opt/app/website/static/about.csv /opt/app/website/kinbank.sqlite3
RUN csvs-to-sqlite  /opt/app/website/static/website_parameters.csv /opt/app/website/kinbank.sqlite3
RUN python /opt/app/website/scripts/bib_to_csv.py --bib /opt/app/website/kinbank/kinbank/raw/sources.bib --out /tmp/sources.csv
RUN csvs-to-sqlite /tmp/sources.csv /opt/app/website/kinbank.sqlite3
RUN python /opt/app/website/manage.py makemigrations
RUN python /opt/app/website/manage.py migrate
RUN python /opt/app/website/manage.py collectstatic --noinput

# run gunicorn
EXPOSE ${PORT:-8010}
ENTRYPOINT ["/opt/app/website/deploy/gunicorn_starter.sh"]

#EXPOSE 8020
#ENTRYPOINT ["/opt/app/gunicorn_starter.sh"]
