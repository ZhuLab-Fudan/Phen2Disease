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
from collections import defaultdict
import json
import pickle
# import pandas as pd
import math

import os
from collections import defaultdict
import json



########patient2disease_json
path_base="../../../../src/result"

path_disease_result=path_base+"/"+"diseaserank/result"
########################################################################################
path_gene_finally="../../../../src/utils/GeneRankResult/finally"

#disease2zscore_json

with open(path_disease_result + "/" + "Phen2Disease_patient_result.json") as fp:
    phen2disease_patient = json.load(fp)

with open(path_disease_result + "/" + "Phen2Disease_double_result.json") as fp:
    phen2disease_double = json.load(fp)

# with open(path_disease_result + "/" + "Phen2Disease_disease_result.json") as fp:
#     phen2disease_disease = json.load(fp)

phen2disease_patient_zscore = defaultdict(dict)

for patient in phen2disease_patient:
    patient_score_list = []
    for gene in phen2disease_patient[patient]:
        patient_score_list.append(float(phen2disease_patient[patient][gene]))
    patient_score_mean = np.array(patient_score_list).mean()
    patient_score_std = np.std(np.array(patient_score_list), ddof=1)
    for gene in phen2disease_patient[patient]:
        phen2disease_patient_zscore[patient][gene] = float(
            (float(phen2disease_patient[patient][gene]) - patient_score_mean) / patient_score_std)

# phen2disease_disease_zscore = defaultdict(dict)
#
# for patient in phen2disease_disease:
#     patient_score_list = []
#     for gene in phen2disease_disease[patient]:
#         patient_score_list.append(float(phen2disease_disease[patient][gene]))
#     patient_score_mean = np.array(patient_score_list).mean()
#     patient_score_std = np.std(np.array(patient_score_list), ddof=1)
#     for gene in phen2disease_disease[patient]:
#         phen2disease_disease_zscore[patient][gene] = float(
#             (float(phen2disease_disease[patient][gene]) - patient_score_mean) / patient_score_std)

phen2disease_double_zscore = defaultdict(dict)

for patient in phen2disease_double:
    patient_score_list = []
    for gene in phen2disease_double[patient]:
        patient_score_list.append(float(phen2disease_double[patient][gene]))
    patient_score_mean = np.array(patient_score_list).mean()
    patient_score_std = np.std(np.array(patient_score_list), ddof=1)
    for gene in phen2disease_double[patient]:
        phen2disease_double_zscore[patient][gene] = float(
            (float(phen2disease_double[patient][gene]) - patient_score_mean) / patient_score_std)


phen2disease_zscore_integrated_sum = defaultdict(dict)

for patient in phen2disease_double_zscore:
    for gene in phen2disease_double_zscore[patient]:
        phen2disease_zscore_integrated_sum[patient][gene] = phen2disease_patient_zscore[patient][gene] + \
                                                            phen2disease_double_zscore[patient][gene]

######diseasezscore2genezscore_json

with open("../../../../data/association/Gene-Disease/disease2genecard2021.json") as fp:
        disease2card = json.load(fp)

with open("../../../../data/association/Gene-Disease/genecard2disease2021.json") as fp:
        card2disease = json.load(fp)

    ########################################################################################

similarity_matrix = phen2disease_zscore_integrated_sum

similarity_matrix_combine = defaultdict(dict)
similarity_matrix_new = defaultdict(dict)

for patient in similarity_matrix:
    for disease in similarity_matrix[patient]:
        if disease in disease2card.keys():
            for genecard in disease2card[disease]:
                similarity_matrix_new[patient][genecard] = 0

for patient in similarity_matrix_new:
    for genecard in similarity_matrix_new[patient]:
        score_list = []
        if genecard in card2disease.keys():
            for disease in card2disease[genecard]:
                if disease in similarity_matrix[patient]:
                    # print(similarity_matrix[disease_1][disease_2])
                    score_list.append(similarity_matrix[patient][disease])
        # print(score_list)
        if np.array(score_list).shape[0] == 0:
            genescore = 0
        else:
            genescore = np.array(score_list).max()
        similarity_matrix_new[patient][genecard] = similarity_matrix_new[patient][genecard] + genescore

for patient in similarity_matrix_new:
    for genecard in similarity_matrix_new[patient]:
        similarity_matrix_combine[patient][genecard] = similarity_matrix_new[patient][genecard]

with open(path_gene_finally + "/" + "Phen2Disease_integrated_result.json", 'w') as fp:
    json.dump(similarity_matrix_combine, fp, indent=2)




