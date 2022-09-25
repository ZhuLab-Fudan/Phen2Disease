# Phen2Disease

Phen2Disease: A Phenotype-driven Semantic Similarity-based Integrated Model for Disease and Gene Prioritization

# Precessing

Extract data/diseaselist.rar file to the current folder

Place the patient HPO files under data/patient

Turn to src/model/Phen2Disease folder and run:

(1) Phen2Disease-patient.py, Phen2Disease-double.py, (Phen2Disease-disease.py (Can be run optionally))

(2) Get the disease sorting results of each case in the corresponding folder of src/result/diseaserank folder

# Disease Prioritization

(1) Turn to src/model/Similarityscore/disease_integrated folder in order to run:

score2disease_patient.py, score2disease_double.py , (score2disease_disease.py (Can be run optionally))

In src/result/diseaserank/result folder you can get the json file of diseases prioritization files after merging cases

(2) Run disease_integrated.py

Turn to src/utils/DiseaseRankResult/finally folder you can get the final json file of the integrated of disease ranking results (Phen2Disease_integrated_result.json)

# Gene Prioritization

(1) Turn to src/model/Similarityscore/gene_integrated folder in order to run:

score2disease_patient.py, score2disease_double.py , (score2disease_disease.py (Can be run optionally))

In src/result/diseaserank/result folder you can get the json file of diseases prioritization files after merging cases

(2) Run gene_integrated.py

Turn to src/utils/GeneRankResult/finally folder you can get the final json file of the integrated of gene ranking results (Phen2Disease_integrated_result.json)

# Data Cohort

For the Data Cohorts 1-6, please see£º

Cohort 1: https://zenodo.org/record/3905420

Cohort 2: https://academic.oup.com/nargab/article/2/2/lqaa032/5843800#supplementary-data

Cohort 3: https://ars.els-cdn.com/content/image/1-s2.0-S0002929721004638-mmc3.xlsx

Cohort 4: https://ars.els-cdn.com/content/image/1-s2.0-S0002929721004638-mmc4.xlsx

Cohort 5: https://ars.els-cdn.com/content/image/1-s2.0-S0002929721004638-mmc5.xlsx

Cohort 6: https://academic.oup.com/bib/article/23/2/bbac019/6521702?login=true#supplementary-data

