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


with open(path_result + "/" + "Phen2Disease_patient_result.json") as fp:
    phen2disease_patient = json.load(fp)

with open(path_result + "/" + "Phen2Disease_double_result.json") as fp:
    phen2disease_double = json.load(fp)

# with open(path_result + "/" + "Phen2Disease_disease_result.json") as fp:
#     phen2disease_disease = json.load(fp)


phen2disease_integrated_sum = defaultdict(dict)

for patient in phen2disease_double:
    for gene in phen2disease_double[patient]:
        phen2disease_integrated_sum[patient][gene] = phen2disease_patient[patient][gene] + \
                                                            phen2disease_double[patient][gene]

# with open(path_result + "/" + "Phen2Disease_integrated_result.json", 'w') as fp:
#     json.dump(phen2disease_integrated_sum, fp, indent=2)


with open(path_finally + "/" + "Phen2Disease_integrated_result.json", 'w') as fp:
    json.dump(phen2disease_integrated_sum, fp, indent=2)




