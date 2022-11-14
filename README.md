# Phen2Disease

Phen2Disease: A Phenotype-driven Semantic Similarity-based Integrated Model for Disease and Gene Prioritization

Please follow the following steps to run the three examples provided in the date/patient folder (or Place your patient HPO files into the folder data/patient folder). 


# PreProcessing

Extract the data/diseaselist.rar file to a current folder where you choose

Get the similarity_matrix file at:
https://drive.google.com/file/d/1CSYfDj5fG9SsosIDlG-hLAoKp9eMHxjH/view?usp=share_link
Put the downloaded matrix file in the data folder

Extract the data/matrix/lin_similarity_matrix.json.gz file to your chosen current folder

Go to the src/model/Phen2Disease folder:

(1) run Phen2Disease-patient.py, and Phen2Disease-double.py, (Phen2Disease-disease.py can be run optionally)

(2) retrieve the disease sorting results of each case from the corresponding folder of src/result/diseaserank 


# Disease Prioritization

(1) Go to the folder of src/model/Similarityscore/disease_integrated folder and run:

score2disease_patient.py, and score2disease_double.py, (score2disease_disease.py can be run optionally)

In the src/result/diseaserank/result folder, and you can get the json file of diseases prioritization files after merging cases.

(2) Run disease_integrated.py

Go to the src/utils/DiseaseRankResult folder, and you can get final files of the integrated disease ranking results.


# Gene Prioritization

(1) Go to the src/model/Similarityscore/gene_integrated folder and run:

score2disease_patient.py, and score2disease_double.py, (score2disease_disease.py can be run optionally))

In the src/result/diseaserank/result folder, you can get the json file of diseases prioritization files after merging cases.

(2) Run gene_integrated.py

Go to the src/utils/GeneRankResult folder, and you can get final files of the integrated gene ranking results.

# Data Cohorts

For the Data Cohorts 1-6, you can find them at the following sites:

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

Phen2Gene: https://phen2gene.wglab.org

Phenolyzer: https://phenolyzer.wglab.org

Phenolyzer package: https://github.com/WGLab/phenolyzer


# Citation

Zhai, W., Huang, X., Shen, N., & Zhu, S. Phen2Disease: A Phenotype-driven Semantic Similarity-based Integrated Model for Disease and Gene Prioritization. In submission.

