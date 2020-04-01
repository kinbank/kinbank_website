KINBANK_REPO=https://github.com/SimonGreenhill/kinbank.git


$(KINBANK):
	mkdir -p data
	git clone $(KINBANK_REPO) $@


help:
	@echo "1. Run 'make install' to install the python requirements & set up virtual environment"

env:
	python3 -m venv myvenv
	./myvenv/bin/python ./myvenv/bin/pip3 install -r requirements.txt

install: env
	git clone https://github.com/SimonGreenhill/kinbank.git

data:
	cd ./kinbank && git pull
	cd ./kinbank/kinbank/cldf/ && csvs-to-sqlite *.csv ../../../kinbank.sqlite3
	# still need to get source.bib into the db

