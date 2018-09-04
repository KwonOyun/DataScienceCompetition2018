import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Dataset = []
d1 = [[2345,34,45],[3456,4,5],[4567,7,8],[5678, 23, 63]]
X = [[10,20,30],[2,3,4], [5,6,8]]
Y = [14565, 654, 765]

# X = np.array(X).reshape(-1,1)
X = np.array(X)
Y = np.array(Y)
# Y = Y.reshape(-1,1)
print(X.shape,Y.shape)

model = LinearRegression()
model = model.fit(X, Y)

beta_1 = model.coef_[0]
beta_2 = model.coef_[1]
beta_3 = model.coef_[2]
beta_0 = model.intercept_
print("Y =",beta_0,beta_1,"x1+", beta_2,"x2+",beta_3,"x3")


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
# print(kwon)
a = np.mean(Dataset, axis=0)
# print(a)

