import argparse
import csv
import bibtexparser

parser = argparse.ArgumentParser(description='Convert sources.bib to sources.csv for loading into SQLite')
parser.add_argument('--bib', required=True, help='Path to sources.bib')
parser.add_argument('--out', required=True, help='Output path for sources.csv')
args = parser.parse_args()

with open(args.bib, encoding='utf-8') as f:
    db = bibtexparser.load(f)

with open(args.out, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['BIBTEXKEY', 'AUTHOR', 'YEAR'])
    writer.writeheader()
    for entry in db.entries:
        writer.writerow({
            'BIBTEXKEY': entry.get('ID', ''),
            'AUTHOR': entry.get('author', ''),
            'YEAR': entry.get('year', ''),
        })

print(f"Wrote {len(db.entries)} entries to {args.out}")
