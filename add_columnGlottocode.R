# /usr/bin/Rscript

library(stringr)

# add a glottocode column
d = read.csv('./kinbank/kinbank/cldf/forms.csv')
d$glottocode = stringr::str_extract(d$Language_ID, "(morgan|[a-z]{4})[0-9]{4}[a-z]?") 
write.csv(d, 'kinbank/kinbank/cldf/forms.csv', 	row.names = FALSE)