# Phen2Disease

A Phenotype-driven Semantic Similarity-based Integrated Model for Disease and Gene Prioritization

# Precessing

Extract data/diseaselist.rar file to the current folder

The patient HPO files are placed under data/patient in order

Turn to src/model/Phen2Disease folder and run:

Phen2Disease-patient.py, Phen2Disease-double.py, (Phen2Disease-disease.py (Can be run optionally))

Get the disease sorting results of each case in the corresponding folder of src/result/diseaserank folder

# Disease Prioritization
(1) Turn to src/model/Similarityscore/disease_integrated folder in order to run:

score2disease_patient.py, score2disease_double.py , (score2disease_disease.py (Can be run optionally))

In src/result/diseaserank/result folder you can get the json file of diseases prioritization files after merging cases

(2) Run disease_integrated.py

Turn to src/utils/DiseaseRankResult/finally folder you can get the final json file of the integrated of disease ranking results (phen2disease_integrated_result.json)

# Gene Prioritization

(1) Turn to src/model/Similarityscore/gene_integrated folder in order to run:

score2disease_patient.py, score2disease_double.py , (score2disease_disease.py (Can be run optionally))

In src/result/diseaserank/result folder you can get the json file of diseases prioritization files after merging cases

(2) Run gene_integrated.py

Turn to src/utils/GeneRankResult/finally folder you can get the final json file of the integrated of gene ranking results (phen2disease_integrated_result.json)
