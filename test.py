import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Dataset = []
d1 = [[2345,34,45],[3456,4,5],[4567,7,8],[5678, 23, 63]]

X = np.array(d1)

Train_X = X[:, 1:3]
Train_Y = X[:, 0:1]
# X = X.reshape(-1,1)

print(X)
print(Train_X)
print(Train_Y)
# print(Y)
# plt.scatter(X,Y)
# plt.show()

model = LinearRegression()
model.fit(Train_X,Train_Y)
beta_1 = model.coef_[0]  #기울기
beta_2 = model.coef_[1]
beta_0 = model.intercept_  #y절편

# print(beta_0, beta_1, beta_2)
# y_new = model.predict(100)  #구축된 모델에 대해 임의의 값 예측
# print(y_new)

Dataset = []
d1 = [1,2,3]
d2 = [3,4,5]

Dataset.append(d1)
Dataset.append(d2)
Dataset.append([6,7,8])
kwon = np.array(Dataset)
a = np.mean(Dataset, axis=0)

