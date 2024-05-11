from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from target_encoding import TargetEncoder
from category_encoders import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import time
import os
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

file_target = []
file_feature_type = []
file_feature_size = []
xlsx_url = 'D:\\100.xlsx'
xlsx_file = pd.read_excel(xlsx_url,usecols='B:D')
file_feature_type = xlsx_file.iloc[:, [0]].values
file_feature_size = xlsx_file.iloc[:, [1]].values
file_target = xlsx_file.iloc[:, [2]].values
for i in range(len(file_target)):
    if file_target[i] == 'BZIP2':
        file_target[i] = 0

    elif file_target[i] == 'PPMD':
        file_target[i] = 1
    elif file_target[i] == 'BROTLI':
        file_target[i] = 2
    else:
        file_target[i] = 3
file_target = file_target.astype('int')
enc = TargetEncoder()
enc.fit(file_feature_type, file_target)
targetEnc_train = enc.transform_train(file_feature_type, file_target)
ohe = OneHotEncoder()
ohe.fit(file_feature_type)
oneHot_train = ohe.transform(file_feature_type)
ss = StandardScaler()
mm = MinMaxScaler(feature_range=(0, 1))
ss.fit(file_feature_size)
ss_data = ss.transform(file_feature_size)
mm_data = mm.fit_transform(file_feature_size)
file_feature = np.hstack((oneHot_train, ss_data))
number=1000
feature_train, feature_test = file_feature[:number],file_feature[number:]
target_train, target_test = file_target[:number],file_target[number:]
target_train = target_train.ravel()
clf = KNeighborsClassifier(n_neighbors=11)
clf.fit(feature_train, target_train)
predict_results = clf.predict(feature_test)
'''
print("KNeighbors:",accuracy_score(target_test,predict_results),end="\t")
'''
cm = confusion_matrix(target_test, predict_results)
print("Confusion Matrix:")
print(cm)


recall = recall_score(target_test, predict_results, average='weighted')
f1 = f1_score(target_test, predict_results, average='weighted')
precision=precision_score(target_test, predict_results,average='weighted')
# 可视化混淆矩阵
print("recall:",recall,end="\t")
print("f1:",f1,end="\t")
print("precision:",precision)
#joblib.dump(value=clf, filename="D:\\100_KNeighbors.pkl")
clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=10)
clf.fit(feature_train, target_train)
predict_results = clf.predict(feature_test)
print("DecisionTree:",accuracy_score(predict_results, target_test),end="\t")
recall = recall_score(target_test, predict_results, average='weighted')
f1 = f1_score(target_test, predict_results, average='weighted')
precision=precision_score(target_test, predict_results,average='weighted')
# 可视化混淆矩阵
print("recall:",recall,end="\t")
print("f1:",f1,end="\t")
print("precision:",precision)
#joblib.dump(value=clf, filename="D:\\100_DecisionTree.pkl")
gnb = BernoulliNB()
gnb.fit(feature_train, target_train)
predict_results = gnb.predict(feature_test)
print("BernoulliNB:",accuracy_score(predict_results, target_test),end="\t")
recall = recall_score(target_test, predict_results, average='weighted')
f1 = f1_score(target_test, predict_results, average='weighted')
precision=precision_score(target_test, predict_results,average='weighted')
# 可视化混淆矩阵
print("recall:",recall,end="\t")
print("f1:",f1,end="\t")
print("precision:",precision)
#joblib.dump(value=gnb, filename="D:\\100_BernoulliNB.pkl")
rfc = RandomForestClassifier(n_estimators=7)
rfc.fit(feature_train, target_train)
predict_results = rfc.predict(feature_test)
print("RandomForest:",accuracy_score(predict_results, target_test),end="\t")
recall = recall_score(target_test, predict_results, average='weighted')
f1 = f1_score(target_test, predict_results, average='weighted')
precision=precision_score(target_test, predict_results,average='weighted')
# 可视化混淆矩阵
print("recall:",recall,end="\t")
print("f1:",f1,end="\t")
print("precision:",precision)
#joblib.dump(value=rfc, filename="D:\\100_RandomForest.pkl")

from sklearn.ensemble import GradientBoostingClassifier
rfc =  GradientBoostingClassifier()
rfc.fit(feature_train, target_train)
predict_results = rfc.predict(feature_test)
print("GradientBoosting:",accuracy_score(predict_results, target_test),end="\t")
recall = recall_score(target_test, predict_results, average='weighted')
f1 = f1_score(target_test, predict_results, average='weighted')
precision=precision_score(target_test, predict_results,average='weighted')
# 可视化混淆矩阵
print("recall:",recall,end="\t")
print("f1:",f1,end="\t")
print("precision:",precision)
#joblib.dump(value=rfc, filename="D:\\100_GradientBoosting.pkl")
from sklearn import svm
rfc =  svm.SVC(C=12)
rfc.fit(feature_train, target_train)
predict_results = rfc.predict(feature_test)
print("SVM:",accuracy_score(predict_results, target_test),end="\t")
recall = recall_score(target_test, predict_results, average='weighted')
f1 = f1_score(target_test, predict_results, average='weighted')
precision=precision_score(target_test, predict_results,average='weighted')
# 可视化混淆矩阵
print("recall:",recall,end="\t")
print("f1:",f1,end="\t")
print("precision:",precision)
#joblib.dump(value=rfc, filename="D:\\100_svm.pkl")
from sklearn.ensemble import AdaBoostClassifier

rfc = AdaBoostClassifier()
rfc.fit(feature_train, target_train)
predict_results = rfc.predict(feature_test)
print("AdaBoost:",accuracy_score(predict_results, target_test),end="\t")
recall = recall_score(target_test, predict_results, average='weighted')
f1 = f1_score(target_test, predict_results, average='weighted')
precision=precision_score(target_test, predict_results,average='weighted')
# 可视化混淆矩阵
print("recall:",recall,end="\t")
print("f1:",f1,end="\t")
print("precision:",precision)







