# Phen2Disease

Phen2Disease: A Phenotype-driven Semantic Similarity-based Integrated Model for Disease and Gene Prioritization

# Precessing

Extract data/diseaselist.rar file to the current folder

Extract data/matrix/lin_similarity_matrix.json.gz file to the current folder

Place the patient HPO files under data/patient

Turn to src/model/Phen2Disease folder and run:

(1) Phen2Disease-patient.py, Phen2Disease-double.py, (Phen2Disease-disease.py (Can be run optionally))

(2) Get the disease sorting results of each case in the corresponding folder of src/result/diseaserank folder

# Disease Prioritization

(1) Turn to src/model/Similarityscore/disease_integrated folder in order to run:

score2disease_patient.py, score2disease_double.py , (score2disease_disease.py (Can be run optionally))

In src/result/diseaserank/result folder you can get the json file of diseases prioritization files after merging cases

(2) Run disease_integrated.py

Turn to src/utils/DiseaseRankResult/finally folder you can get the final file of the integrated of disease ranking results

# Gene Prioritization

(1) Turn to src/model/Similarityscore/gene_integrated folder in order to run:

score2disease_patient.py, score2disease_double.py , (score2disease_disease.py (Can be run optionally))

In src/result/diseaserank/result folder you can get the json file of diseases prioritization files after merging cases

(2) Run gene_integrated.py

Turn to src/utils/GeneRankResult/finally folder you can get the final file of the integrated of gene ranking results

# Data Cohort

For the Data Cohorts 1-6, please see:

Cohort 1 [1]: https://zenodo.org/record/3905420

Cohort 2 [2]: https://academic.oup.com/nargab/article/2/2/lqaa032/5843800#supplementary-data

Cohort 3 [3]: https://ars.els-cdn.com/content/image/1-s2.0-S0002929721004638-mmc3.xlsx

Cohort 4 [3]: https://ars.els-cdn.com/content/image/1-s2.0-S0002929721004638-mmc4.xlsx

Cohort 5 [3]: https://ars.els-cdn.com/content/image/1-s2.0-S0002929721004638-mmc5.xlsx

Cohort 6 [4]: https://academic.oup.com/bib/article/23/2/bbac019/6521702?login=true#supplementary-data

# References

[1] Robinson PN, Ravanmehr V, Jacobsen JOB, et al. Interpretable Clinical Genomics with a Likelihood Ratio Paradigm. Am J Hum Genet. 2020 Sep 3;107(3):403-417.

[2] Zhao, M., Havrilla, et al. Phen2Gene: rapid phenotype-driven gene prioritization for rare diseases. NAR Genom Bioinform. 2020 Jun;2(2):lqaa032.

[3] Chen, Z., Zheng, et al. PhenoApt leverages clinical expertise to prioritize candidate genes via machine learning. Am J Hum Genet. 2022 Feb 3;109(2):270-281.

[4] Yuan X, Wang J, Dai B, et al. Evaluation of phenotype-driven gene prioritization methods for Mendelian diseases. Brief Bioinform. 2022 Mar 10;23(2):bbac019.

# Web Resources for Comparison Methods

AMELIE: https://amelie.stanford.edu

LIRICAL: https://lirical.readthedocs.io/en/latest

PhenoApt: https://www.phenoapt.org

Phrank package: https://pypi.org/project/phrank

Phenolyzer: https://phenolyzer.wglab.org

Phenolyzer package: https://github.com/WGLab/phenolyzer


# Citation

Zhai, W., Huang, X., Shen, N., & Zhu, S. Phen2Disease: A Phenotype-driven Semantic Similarity-based Integrated Model for Disease and Gene Prioritization. In submission.

