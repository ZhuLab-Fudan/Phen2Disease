#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import pandas as pd
import pickle
from collections import defaultdict
from functools import reduce
from sklearn.preprocessing import MultiLabelBinarizer
import pickle
from multiprocessing import Pool
import numpy as np
import math
import os

#####The path where the project is placed
path_main="../../../.."


path_result=path_main+"/"+"src/result/diseaserank/result"

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")

    else:
        print("---  The folder already exists  ---")

file_path_result = path_result
mkdir(file_path_result)

########################################################################################

path_patient_score = path_main+"/"+"src/result/diseaserank/disease"
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


