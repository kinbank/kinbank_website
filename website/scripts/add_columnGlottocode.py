
import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(description="Add glottocode column to forms.csv")
parser.add_argument('--forms-path', type=str, default=None, help='Path to forms.csv')
args = parser.parse_args()

forms_path = args.forms_path

d = pd.read_csv(forms_path)
d['glottocode'] = d['Language_ID'].str.extract("([a-z]{4}[0-9]{4}[a-z]?)$", expand=False)
d.to_csv(forms_path, index=False)
