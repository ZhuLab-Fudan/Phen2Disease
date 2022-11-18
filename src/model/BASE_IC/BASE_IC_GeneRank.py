#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import pickle
from functools import reduce
from collections import defaultdict
from sklearn.preprocessing import MultiLabelBinarizer
from multiprocessing import Pool
import numpy as np
import math
from ontology import HumanPhenotypeOntology
from ontology import get_root, get_subontology
import os
import json


#####The path where the project is placed
path_main="../../.."


path_config= path_main + "/" + "config/preprocessing"
#
with open(path_config+"/"+"split_dataset_lableler.json") as fp:
    config= json.load(fp)
# load various versions of HPO
# ontology_t0 = HumanPhenotypeOntology(config["ontology"]["time0"]["path"],
#                                      version=config["ontology"]["time0"]["version"])
ontology_t1 = HumanPhenotypeOntology(config["ontology"]["time1"]["path"],
                                     version=config["ontology"]["time1"]["version"])


# ########read association
path_association=path_main + "/" + "data/association/Disease-Hpo"
with open(path_association+"/"+"disease2hpo20210413.json") as fp:
    new_annotation = json.load(fp)



# ########read patient_data
path_gene = path_main + "/" + "data/genelist"
path_patient=path_main + "/" + "data/patient"
path_result = path_main + "/" + "src/model/BASE_IC/GeneRank"


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")

    else:
        print("---  The folder already exists  ---")

file_path_result = path_result
mkdir(file_path_result)




# global variable, ancestors of each HPO term
ancestors = dict()
# global variable, frequency of terms
freq = None
# global variable, information content of HPO terms
ic = None



def lin_sim(x):
    """
    Lin measure, see Lin D. An information-theoretic definition of
    similarity. In: ICML, vol. Vol. 98, no. 1998; 1998. p. 296–304.
    :param x: tuple of index name, i.e. (row_term, col_term)
    :return: similarity
    """
    global ancestors
    global ic

    term_a, term_b = x
    # set values on the diagonal to 1
    if term_a == term_b:
        return 1
    # ancestors of term_a
    ancestors_a = ancestors[term_a]
    # ancestors of term_b
    ancestors_b = ancestors[term_b]
    # all common ancestors of term_a and term_b (and also in terms)
    common_ancestors = list(ancestors_a & ancestors_b)
    # information content of most informative common ancestor
    ic_mica = ic[common_ancestors].max()
    # similarity between term_a and term_b
    sim = 2 * ic_mica / (ic[term_a] + ic[term_b])
    return sim




propagated_annotation = dict()
for disease in new_annotation:
    propagated_annotation[disease] = list(
        ontology_t1.transfer(new_annotation[disease]))
        # - {get_root()} -set(get_subontology(ontology_t1.version)))


propagated_annotation_new = defaultdict(set)
for disease in propagated_annotation:
    for term in propagated_annotation[disease]:
        propagated_annotation_new[term].add(disease)

test_dataset=propagated_annotation_new

term_list = list(test_dataset.keys())

disease_list= set(reduce(lambda a, b: set(a) | set(b),
                          test_dataset.values()))

mlb = MultiLabelBinarizer()
df_test_dataset = pd.DataFrame(mlb.fit_transform(test_dataset.values()),
                               columns=mlb.classes_,
                               index=test_dataset.keys()).reindex(
                               columns=disease_list, index=term_list, fill_value=0).transpose()

test_annotation = df_test_dataset.reindex(
        index=disease_list, columns=term_list, fill_value=0)


test_annotation = test_annotation.loc[:, (test_annotation != 0).any(axis=0)]
# remove rows containing only zeros
test_annotation = test_annotation[(test_annotation.T != 0).any()]


total_disease = len(test_annotation.index)
# sum over the diseases to calculate the frequency of terms
freq = test_annotation.sum(axis=0)/total_disease
# information content of each HPO term
ic = -freq.apply(math.log2)


########################################################################################

#########inheritance set
sp_term="HP:0000118"
inheritance_list=[]
inheritance_list_new=[]
root_set={get_root()}
for term in root_set:
    inheritance_list.append(term)
sub_root_set=set(get_subontology(ontology_t1.version))-{sp_term}
for term in sub_root_set:
    inheritance_list.append(term)
for term in sub_root_set:
    for term_d in ontology_t1.get_descendants([term]):
        inheritance_list.append(term_d)



#read path
files_gene_folder = os.listdir(path_gene)
files_patient_folder = os.listdir(path_patient)

term_list_sets=set(term_list)

for term in term_list_sets:
    ancestors[term] = ontology_t1.get_ancestors([term])
                      # - {get_root()} -set(get_subontology(ontology_t1.version))


for file in files_patient_folder:
    file1= str(file)
    patient_name_str = str(file1)
    termlist_patient=pd.read_csv(path_patient+"/"+file1,header=None)

    patient2gene_similarity_score = defaultdict(dict)

    for file_compare in files_gene_folder:
        gene_name_str = str(file_compare)
        file2 = str(file_compare)
        termlist_gene = pd.read_csv(path_gene + "/" + file2, header=None)

        gene_term_list = list(termlist_gene[0].values)
        patient_term_list_ORI = list(termlist_patient[0].values)
        ################################################
        ##except term
        patient_term_list = []
        for term in patient_term_list_ORI:
            if term in term_list:
                patient_term_list.append(term)
        patient_term_list = list(patient_term_list)
        ################################################
        ################################################
        ####Filter
        gene_term_list_filter = []
        patient_term_list_filter = []
        # gene_term_list
        # patient_term_list
        for term in gene_term_list:

            judgment = 0
            if term in inheritance_list:
                judgment = judgment + 1
            term_gene_filter_temp_list = []
            for term_d in ontology_t1.get_descendants([term]):
                term_gene_filter_temp_list.append(term_d)
            for term_f in gene_term_list:
                if term_f in term_gene_filter_temp_list:
                    judgment = judgment + 1
                else:
                    judgment = judgment + 0
            if judgment == 0:
                gene_term_list_filter.append(term)

        for term in patient_term_list:

            judgment = 0
            if term in inheritance_list:
                judgment = judgment + 1
            term_patient_filter_temp_list = []
            for term_d in ontology_t1.get_descendants([term]):
                term_patient_filter_temp_list.append(term_d)
            for term_f in patient_term_list:
                if term_f in term_patient_filter_temp_list:
                    judgment = judgment + 1
                else:
                    judgment = judgment + 0
            if judgment == 0:
                patient_term_list_filter.append(term)
        ################################################

        same_ic_list = list(set(patient_term_list_filter) & set(gene_term_list_filter))

        merge_score = 0
        for term in same_ic_list:
            merge_score = merge_score + ic[term]

        patient2gene_similarity_score[patient_name_str][gene_name_str] = merge_score



    patient_rank_df = pd.DataFrame()
    patient_gene_list = []
    patient_score_list=[]
    for gene in patient2gene_similarity_score[patient_name_str]:
        patient_gene_list.append(gene)
        patient_score_list.append(patient2gene_similarity_score[patient_name_str][gene])


    patient_rank_df["gene"]=patient_gene_list
    patient_rank_df["score"]=patient_score_list
    patient_rank_df.sort_values(by="score", inplace=True, ascending=False)
    patient_rank_df.to_csv(path_result+"/"+patient_name_str+".csv",index=None)
