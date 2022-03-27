#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split protein list into three parts: train set, ltr set, and test set.
We will get three annotation datasets, three protein lists, and term list.
Besides, we will split HPO terms into several groups according to frequency.
"""
import json
import pandas as pd
import pickle
from collections import defaultdict
from functools import reduce
from collections import defaultdict
from sklearn.preprocessing import MultiLabelBinarizer
import json
import pickle
from multiprocessing import Pool
# import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score

import math
from collections import defaultdict
from functools import reduce
from ontology import HumanPhenotypeOntology
from ontology import get_root, get_subontology
import os
from collections import defaultdict
import json
import pickle
from functools import reduce
import numpy as np
import pandas as pd


path_base="../../../../src/result/diseaserank"

path_result=path_base+"/"+"result"
########################################################################################

path_patient_score = path_base+"/"+"disease"
files_folder = os.listdir(path_patient_score)

similarity_matrix_combine = defaultdict(dict)
for file1 in files_folder:
    file_str = str(file1)
    patient_name_str = str(file_str)

    similarity_matrix_new = defaultdict(dict)

    with open("%s/%s" % (path_patient_score, file1)) as fp:
        similarity_matrix = json.load(fp)

    for patient in similarity_matrix:
        for disease in similarity_matrix[patient]:
            similarity_matrix_new[patient][disease] = 0

    for patient in similarity_matrix_new:
        for disease in similarity_matrix_new[patient]:
            similarity_matrix_new[patient][disease] = similarity_matrix_new[patient][disease] + \
                                                      similarity_matrix[patient][disease]

    for patient in similarity_matrix_new:
        for disease in similarity_matrix_new[patient]:
            similarity_matrix_combine[patient][disease] = similarity_matrix_new[patient][disease]

with open(path_result + "/" + "Phen2Disease_disease_result.json", 'w') as fp:
    json.dump(similarity_matrix_combine, fp, indent=2)


