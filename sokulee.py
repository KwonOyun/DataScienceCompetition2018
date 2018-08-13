from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans
import glob
Allfeature = []
AllDataset = []#means
personIndex = 0
for file in glob.glob("C:\\Users\\SUKA\\Desktop\\2018 SOKULEE_Fitbit_Data\\*.xls"):
    ActiveData = pd.read_excel(file,
                               sheet_name='활동')
    SleepData = pd.read_excel(file,
                              sheet_name='수면')
    if personIndex==15:
        print(file)
    ActiveData = np.array(ActiveData)
    dataSet = []
    FeatureSet = []
    for i in range(len(ActiveData)):
        row = []
        featurerow = [personIndex]
        for j in range(len(ActiveData[i])):
            if j != 0 and j!=4 and type(ActiveData[i][j]) is str:
                featurerow.append(int(ActiveData[i][j].replace(",", "")))
                row.append(int(ActiveData[i][j].replace(",", "")))
            elif j != 0 and  j!=4:
                featurerow.append(int(ActiveData[i][j]))
                row.append(int(ActiveData[i][j]))

        dataSet.append(row)
        Allfeature.append(featurerow)
    AMeans = np.mean(dataSet, axis=0)

    # Allfeature.append(FeatureSet)

    SleepData = np.array(SleepData)
    dataSet = []
    for i in range(len(SleepData)):
        row = []
        for j in range(len(SleepData[i]) - 3):
            if j != 0 and j != 1 and type(SleepData[i][j]) is str:
                row.append(int(SleepData[i][j].replace(",", "")))
            elif j != 0 and j != 1:
                row.append(int(SleepData[i][j]))
        dataSet.append(row)
    SMeans = np.mean(dataSet, axis=0)

    Means = []
    for i in AMeans:
        Means.append(i)
    for i in SMeans:
        Means.append(i)
    AllDataset.append(Means)
    personIndex+=1
AllDataset = np.array(AllDataset)
# Linear Regression
# X = np.array(AllDataset[:,1])
# Y = np.array(AllDataset[:,2])
#
# plt.scatter(X,Y)
# MaxX = int(np.max(X))
# X=X.reshape(-1,1)
#
# lrmodel = LinearRegression()
# lrmodel.fit(X,Y)
# beta_0 = lrmodel.coef_[0]
# beta_1 = lrmodel.intercept_
#
# print(beta_0,beta_1)
# print(np.sum((Y-(X*beta_0+beta_1))**2))
# plt.plot([0,MaxX] ,[beta_1,MaxX*beta_0+beta_1],c="r")
# plt.show()
#############################
Score = []
for row in AllDataset:
    ActiveScore=0
    static =0
    SleepScore = row[8]
    for idx,feature in enumerate(row):
        if idx ==3:
            static = feature
        if idx <7 and idx >3:
            ActiveScore+=feature


    Score.append([ActiveScore/(static+ActiveScore),SleepScore])

Score = np.array(Score)

Score[:,0] = (Score[:,0]-np.min(Score[:,0]))
Score[:, 0] = Score[:,0]  /np.max(Score[:,0])

Score[:,1] = (Score[:,1]-np.min(Score[:,1]))
Score[:, 1] = Score[:,1]  /np.max(Score[:,1])



kmeans = KMeans(n_clusters=4, random_state=0).fit(Score)
labels = (kmeans.predict(Score))

plt.scatter(Score[:,0],Score[:,1],c= labels)
plt.show()

X = np.array(Allfeature)
train_X = X[:,5:8]
train_Y = X[:,2]
lrmodel = LinearRegression()
lrmodel.fit(train_X,train_Y)
beta_0 = lrmodel.coef_[0]
beta_1 = lrmodel.coef_[1]
beta_2 = lrmodel.coef_[2]
beta_3 = lrmodel.intercept_

print(beta_0,beta_1,beta_2,beta_3)
CostArray = []

for idx,x in enumerate(train_X):
    cost = (train_Y[idx] - (x[0]*beta_0+x[1]*beta_1+x[2]*beta_2+beta_3))
    CostArray.append(cost)

CostArray = np.array(CostArray)
criminer = np.argsort(CostArray)

for i in range(20):
    print(X[criminer[len(criminer)-i-1]])

