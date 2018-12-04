from nltk.corpus import semcor
# import pandas as pd
#
# senselist=[]
# indexlist=[]
# for i in range(len(semcor.tagged_sents(tag='both'))):
#     for j in range(len(semcor.tagged_sents(tag='both')[i])):
#         indexlist.append(i)
#         senselist.append(semcor.tagged_sents(tag='both')[i][j].label())
#         print(senselist, indexlist)
#
# dataframe=pd.DataFrame()
# dataframe['senselist']=senselist
# dataframe['indexlist']=indexlist
#
# dataframe.to_csv("sense_export.csv")
# dataframe.to_json("sense_export.json")

# semcor.tagged_sents(tag='sem')[1]#[3].label()
import re
import pandas as pd

flat_list=[]

for i in semcor.tagged_sents(tag='sem'):
    flat_list.append(i)

string = str(flat_list)

export=re.findall(r"Lemma\((.*?)\)", string)

# i=0
# while i < len(semcor.tagged_sents(tag='sem')):
#     export1=re.findall(r"Lemma\((.*?)\)", str(semcor.tagged_sents(tag='sem')[i:i+99]))
#     export=export1+export
#     i+=100

export_df=pd.DataFrame(export)
export_df.to_csv("sense_export_2.csv")

