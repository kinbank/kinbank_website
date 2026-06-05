# KinBank Website

A Django web application for browsing the [KinBank](https://github.com/kinbank/kinbank) dataset — a cross-linguistic database of kinship terminology.

The production site is packaged as a Docker image and hosted on Heroku.

---

## Architecture

- **Web framework**: Django 6.0 served via Gunicorn
- **Database**: SQLite, built from the KinBank CLDF CSV files at image build time
- **Containerisation**: Docker (defined in `Dockerfile` and `heroku.yml`)
- **Hosting**: Heroku (container stack)

---

## Running locally

### Option 1 — Python virtual environment

1. Create the virtual environment and install dependencies:

   ```bash
   make env
   ```

2. Activate the environment:

   ```bash
   source ./myvenv/bin/activate
   ```

3. Build the dataset (see [Dataset creation](#dataset-creation) below):

   ```bash
   make install   # clones the kinbank data repo
   make data      # builds kinbank.sqlite3
   ```

4. Apply migrations and start the development server:

   ```bash
   cd website
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

   The site will be available at `http://127.0.0.1:8000`.

### Option 2 — Docker Compose

Build and run the container locally:

```bash
docker-compose up --build
```

The site will be available at `http://localhost:8010`.

> **Note:** The Docker build clones the KinBank data repository and constructs the SQLite database automatically, so no separate dataset setup step is needed.

---

## Dataset creation

The SQLite database (`kinbank.sqlite3`) is assembled from the upstream [KinBank](https://github.com/kinbank/kinbank) repository and two local CSV files.

**Steps performed by `make data` (and mirrored in the `Dockerfile`):**

1. **Pull the latest KinBank data**

   ```bash
   cd ./kinbank && git pull
   ```

   The KinBank repository stores data in [CLDF](https://cldf.clld.org/) format as a set of CSV files under `kinbank/kinbank/cldf/`.

2. **Add Glottocode column**

   ```bash
   python website/scripts/add_columnGlottocode.py --forms-path ./kinbank/kinbank/cldf/forms.csv
   ```

   This script extracts the [Glottocode](https://glottolog.org/) from the `Language_ID` field in `forms.csv` and writes it as a new `glottocode` column. Glottocodes follow the pattern `[a-z]{4}[0-9]{4}` at the end of the Language_ID string.

3. **Convert CLDF CSVs to SQLite**

   ```bash
   csvs-to-sqlite ./kinbank/kinbank/cldf/*.csv kinbank.sqlite3
   ```

   All CLDF CSV files (forms, languages, parameters, etc.) are loaded into a single SQLite database.

4. **Add supplementary tables**

   ```bash
   csvs-to-sqlite website/kb/static/about.csv kinbank.sqlite3
   csvs-to-sqlite website/static/website_parameters.csv kinbank.sqlite3
   ```

   - `about.csv` — content for the About page
   - `website_parameters.csv` — additional parameter metadata used by the website

5. **Run Django migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## Heroku deployment

Deployment to Heroku uses the container stack via `heroku.yml`, which instructs Heroku to build the `web` process from the `Dockerfile`:

```yaml
build:
  docker:
    web: Dockerfile
```

To deploy:

```bash
heroku stack:set container -a <your-app-name>
git push heroku main
```

Heroku injects a `$PORT` environment variable at runtime; the Gunicorn entrypoint binds to this port automatically.

---

## Cleaning up

To remove the cloned data repository, the generated database, and the virtual environment:

```bash
make clean
```
