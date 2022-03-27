from collections import defaultdict
import json
import pickle
from functools import reduce
import numpy as np
import pandas as pd

from functools import reduce
from collections import defaultdict
from sklearn.preprocessing import MultiLabelBinarizer
# from ontology import HumanPhenotypeOntology



##weight
path_weight="../../../data/weight"
with open(path_weight+"/"+"skewscore.json") as fp:
    skewscore=json.load(fp)
with open(path_weight+"/"+"term_frequency.json") as fp:
    term_frequency=json.load(fp)

term_list=[]
score=[]
for term in skewscore:
    term_list.append(term)
    score.append(skewscore[term])
skew_data = {'HPO':term_list,'skew_score':score} # 两组列元素，并且个数需要相同
skew_df = pd.DataFrame(skew_data)

term_list=[]
score=[]
for term in term_frequency:
    term_list.append(term)
    score.append(term_frequency[term])
frequency_data = {'HPO':term_list,'frequency_score':score} # 两组列元素，并且个数需要相同
frequency_df = pd.DataFrame(frequency_data)

merge_df=pd.merge(skew_df,frequency_df, how='right')

merge_df['skew_score'] = merge_df['skew_score']#.fillna(merge_df['skew_score'].mean())

merge_df['integrated_score']=merge_df['frequency_score']
#

path_association="../../../data/association"
with open(path_association+"/Hpo-Gene/"+"hpo2genecard2021transfer.json") as fp:
  hpo2protein = json.load(fp)
#

with open(path_association+"/Patient/"+"patient2hpo384.json") as fp:
    diease2hpotest = json.load(fp)

term_list_0 = list(hpo2protein.keys())

protein_list = set(reduce(lambda a, b: set(a) | set(b),
                          hpo2protein.values()))
mlb = MultiLabelBinarizer()
transfer_1 = pd.DataFrame(mlb.fit_transform(hpo2protein.values()),
                          columns=mlb.classes_,
                          index=hpo2protein.keys()).reindex(
    columns=protein_list, index=term_list_0, fill_value=0)

# diease2hpotest
diease_list = list(diease2hpotest.keys())

term_list = set(reduce(lambda a, b: set(a) | set(b),
                       diease2hpotest.values()))
mlb = MultiLabelBinarizer()
transfer_2 = pd.DataFrame(mlb.fit_transform(diease2hpotest.values()),
                          columns=mlb.classes_,
                          index=diease2hpotest.keys()).reindex(
    columns=term_list, index=diease_list, fill_value=0).transpose()

# index_id_1 = transfer_1[transfer_1["Q8NCE0"]==1].index.tolist()
# index_id_2 = transfer_2[transfer_2["OMIM:605275"]==1].index.tolist()
diease_to_protein = defaultdict(dict)

for diease in transfer_2.keys():
    for protein in transfer_1.keys():
        index_diease = transfer_2[transfer_2[diease] == 1].index.tolist()
        index_protein = transfer_1[transfer_1[protein] == 1].index.tolist()
        same_df = pd.merge(pd.DataFrame(index_diease), pd.DataFrame(index_protein), how='inner')
        #Weight
        same_df_score=merge_df.loc[merge_df["HPO"].isin(same_df[0])]
        # number_link = same_df.shape[0]
        number_IC=same_df_score["integrated_score"].sum()
        diease_to_protein[diease][protein] = number_IC

path_result="../../../src/utils/GeneRankResult/finally"
with open(path_result+"/"+"BASE_IC_result.json", "w") as fp:
    json.dump(diease_to_protein, fp, indent=2)
