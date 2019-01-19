from nltk.corpus import semcor

flat_list = []
unflat_list = []

for i in semcor.sents():
    placeholder = []
    for word in i:
        placeholder.append(word.lower())
    unflat_list.append(placeholder)
    for j in i:
        flat_list.append(j.lower())


wordlist = list(set(flat_list))


DICT = {}


for i in range(len(unflat_list)):
    for item in wordlist:
        if item in unflat_list[i]:
            DICT.setdefault(item, []).append(i)
print(DICT)

import pandas as pd
df=pd.DataFrame([DICT.keys(),DICT.values()])
df.to_json('export_file_v2.json')
