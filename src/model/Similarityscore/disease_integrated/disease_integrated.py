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


path_base="../../../../src/result/diseaserank"

path_result=path_base+"/"+"result"
########################################################################################
path_finally="../../../../src/utils/DiseaseRankResult/finally"

#disease2zscore_json


with open(path_result + "/" + "Phen2Disease_patient_result.json") as fp:
    phen2disease_patient = json.load(fp)

with open(path_result + "/" + "Phen2Disease_double_result.json") as fp:
    phen2disease_double = json.load(fp)

# with open(path_result + "/" + "Phen2Disease_disease_result.json") as fp:
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
        # phen2disease_zscore_integrated_sum[patient][gene] = phen2disease_patient_zscore[patient][gene] + \
        #                                                     phen2disease_double_zscore[patient][gene] + \
        #                                                     phen2disease_disease_zscore[patient][gene]
        phen2disease_zscore_integrated_sum[patient][gene] = phen2disease_patient_zscore[patient][gene] + \
                                                            phen2disease_double_zscore[patient][gene]  # + \
        # phen2disease_disease_zscore[patient][gene]


with open(path_result + "/" + "phen2disease_integrated_result.json", 'w') as fp:
    json.dump(phen2disease_zscore_integrated_sum, fp, indent=2)


with open(path_finally + "/" + "phen2disease_integrated_result.json", 'w') as fp:
    json.dump(phen2disease_zscore_integrated_sum, fp, indent=2)




