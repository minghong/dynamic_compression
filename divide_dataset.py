from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

file_target = []
file_feature_type = []
file_feature_size = []
xlsx_url = 'D:\\avi.xlsx'
xlsx_file = pd.read_excel(xlsx_url,usecols='B:D')
data = np.array(xlsx_file) 
data_list = data.tolist()  
out=open("D:\\test.txt","w")
number=0
flag={}
for i in  range(len(data_list)):
    flag[i]=0
dic={}

while(number<1000):
    for i in range(0,500):
        dic[i]=0
    for i in range(len(data_list)):
        if(dic[data_list[i][1]//5000]==0 and flag[i]==0):
            for j in data_list[i]:
                out.write(str(j)+"\t")
            out.write("\n")
            dic[data_list[i][1]//5000]=1;flag[i]=1
            number+=1
        else:
            pass
        if(number>=1000):
            break

out.close()