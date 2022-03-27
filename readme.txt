解压data/matrix/ic_similarity_matrix.rar文件到当前文件夹
解压data/diseaselist.rar文件当前文件夹
病人HPO文件依次放在data/patient 下

src/model/Phen2Disease文件夹下依次运行
Phen2Disease-patient.py、Phen2Disease-double.py 、Phen2Disease-disease.py(可以不运行)
在src/result/diseaserank对应文件夹下得到每个case的疾病排序结果

1.疾病优选排序：
(1).src/model/Similarityscore/disease_integrated文件夹下依次运行
score2disease_patient.py、score2disease_double.py 、score2disease_disease.py(可以不运行)
在src/result/diseaserank/result文件夹下得到合并cases之后疾病排序的json文件

(2).运行disease_integrated.py
在src/utils/DiseaseRankResult/finally得到最终的疾病排序集成结果的json文件(phen2disease_integrated_result.json)

2.基因优选排序：
(1).src/model/Similarityscore/gene_integrated文件夹下依次运行
score2disease_patient.py、score2disease_double.py 、score2disease_disease.py(可以不运行)
在src/result/diseaserank/result文件夹下得到合并cases之后的疾病排序的json文件

(2).运行gene_integrated.py
在src/utils/GeneRankResult/finally得到最终的基因排序集成结果的json文件(phen2disease_integrated_result.json)
