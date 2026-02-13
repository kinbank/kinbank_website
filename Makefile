KINBANK_REPO=https://github.com/SimonGreenhill/kinbank.git

$(KINBANK):
	mkdir -p data
	git clone $(KINBANK_REPO) $@

clean:
	rm -rf kinbank/ ./kinbank.sqlite3 ./myvenv

help:
	@echo "1. Run 'make install' to install the python requirements & set up virtual environment"
	@echo "2. open the environment by running source ./myvenv/bin/activate"

env:
	python3 -m venv myvenv
	./myvenv/bin/python ./myvenv/bin/pip3 install -r ./requirements.txt

install: env
	git clone https://github.com/kinbank/kinbank.git

open:
	source ./myvenv/bin/activate

data:
	cd ./kinbank && git pull
	./myvenv/bin/python add_columnGlottocode.py
	cp ./kinbank/kinbank/etc/languages.csv ./kinbank/kinbank/cldf/languages.csv
	./myvenv/bin/csvs-to-sqlite ./kinbank/kinbank/cldf/*.csv ./kinbank.sqlite3
	./myvenv/bin/csvs-to-sqlite  ./website/kb/static/about.csv ./kinbank.sqlite3
	./myvenv/bin/csvs-to-sqlite  ./static/website_parameters.csv ./kinbank.sqlite3
	echo "Remember to makemigrations and migrate"
