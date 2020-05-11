import pandas as pd
from kb.models import Forms

# df = pd.read_csv('kinbank/kinbank/cldf/forms.csv')



# subset to language
gc = "stan1290"
# df = df[df.glottocode == gc]


df = pd.DataFrame(Forms.objects.filter(glottocode = gc).values())

## Seperate M & F speakers
# F Speakers
f_speaker = df[df['parameter_id'].str.contains(r'^f')]
f_speaker = f_speaker[['language_id', 'form', 'comment', 'source', 'parameter_id']]
f_speaker['parameter'] = f_speaker['parameter_id'].str[1:]

# M Speakers
m_speaker = df[df['parameter_id'].str.contains(r'^m')]
m_speaker = m_speaker[['language_id', 'form', 'comment', 'source', 'parameter_id']]
m_speaker['parameter'] = m_speaker['parameter_id'].str[1:]


display_table = pd.merge(f_speaker, m_speaker, on='parameter', how='outer')
#display_table = pd.concat([f_speaker.reset_index(drop=True), m_speaker], axis=1)

display_table = display_table[['parameter', 'form_x', 'form_y', 'source_x', 'source_y']]
#display_table['Source'] = display_table["Source_x"] + "; " + display_table["Source_y"]

source = []
for index, row in display_table.iterrows():
    if row['source_x'] == row['source_y']:
    	source.append(row['source_x'])
    else:
    	source.append(row["source_x"] + "; " + row["source_y"])

display_table['source'] = source
del display_table['source_x']
del display_table['source_y']
display_table.columns = [['kin_category', 'woman_speaking', 'man_speaking', 'source']]

print(display_table)