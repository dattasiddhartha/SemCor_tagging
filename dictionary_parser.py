from nltk.corpus import semcor

# test=[item for sublist in l for item in semcor.sents()[0:5]]
flat_list=[]
# for i in semcor.sents()[0:10]:
for i in semcor.sents():
    flat_list.append(i)
# string = str(semcor.sents()[0:5])
string = str(flat_list)

DICT = {}

LIST  =  string.split('.')

WORDS = list(set(string.lower().replace('.',"").split()))

LIST = [set((x.lower()).split()) for x in LIST]

for i in range(len(LIST)):
    for item in WORDS:
        if item in LIST[i]:
            DICT.setdefault(item, []).append(i)
print(DICT)

import pandas as pd
# # one_line_dict = exDict = {1:1, 2:2, 3:3}
# df = pd.DataFrame.from_dict([DICT])
df=pd.DataFrame([DICT.keys(),DICT.values()])
# df.to_csv('export_file.csv')
df.to_json('export_file.json')
