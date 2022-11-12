#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pandas as pd

from collections import defaultdict
from functools import reduce
import json

# import pandas as pd
import numpy as np


import os
import pickle
# import pandas as pd
import math


#####The path where the project is placed
path_main="../../../.."



########patient2disease_json

path_disease_result=path_main+"/"+"src/result/diseaserank/result"

########################################################################################
path_disease_finally=path_main+"/"+"src/utils/DiseaseRankResult"

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")

    else:
        print("---  The folder already exists  ---")

file_path_disease_finally = path_disease_finally
mkdir(file_path_disease_finally)



with open(path_disease_result + "/" + "Phen2Disease_patient_result.json") as fp:
    phen2disease_patient = json.load(fp)

with open(path_disease_result + "/" + "Phen2Disease_double_result.json") as fp:
    phen2disease_double = json.load(fp)

# with open(path_disease_result + "/" + "Phen2Disease_disease_result.json") as fp:
#     phen2disease_disease = json.load(fp)

phen2disease_integrated_sum = defaultdict(dict)

for patient in phen2disease_double:
    for disease in phen2disease_double[patient]:
        phen2disease_integrated_sum[patient][disease] = phen2disease_patient[patient][disease] + \
                                                            phen2disease_double[patient][disease]


similarity_matrix_combine = defaultdict(dict)

for patient in phen2disease_integrated_sum:
    patient_name=str(patient)

    patient_rank_df = pd.DataFrame()
    patient_disease_list = []
    patient_score_list=[]
    for disease in phen2disease_integrated_sum[patient]:
        patient_disease_list.append(disease)
        patient_score_list.append(phen2disease_integrated_sum[patient][disease])

        similarity_matrix_combine[patient][disease] = phen2disease_integrated_sum[patient][disease]

    patient_rank_df["disease"]=patient_disease_list
    patient_rank_df["score"]=patient_score_list
    patient_rank_df.sort_values(by="score", inplace=True, ascending=False)
    patient_rank_df.to_csv(path_disease_finally + "/" + patient_name+".csv",index=None)



with open(path_disease_finally + "/" + "Phen2Disease_integrated_result.json", 'w') as fp:
    json.dump(similarity_matrix_combine, fp, indent=2)




