KINBANK_REPO=https://github.com/SimonGreenhill/kinbank.git

$(KINBANK):
	mkdir -p data
	git clone $(KINBANK_REPO) $@


help:
	@echo "1. Run 'make install' to install the python requirements & set up virtual environment"
	@echo "2. open the environment by running source ./myvenv/bin/activate"

env:
	python3 -m venv myvenv
	./myvenv/bin/python ./myvenv/bin/pip3 install -r requirements.txt

install: env
	git clone https://github.com/SimonGreenhill/kinbank.git

open:
	source ./myvenv/bin/activate

data:
	cd ./kinbank && git pull
	RScript add_columnGlottocode.R
	RScript bib_tocsv.R
	./myvenv/bin/csvs-to-sqlite ./kinbank/kinbank/cldf/*.csv ./kinbank.sqlite3
	./myvenv/bin/csvs-to-sqlite  ./kb/static/about.csv ./kinbank.sqlite3
	echo "Remember to makemigrations and migrate"
