import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd

SleepData  = pd.read_excel('C:/Users/oyun/Desktop/fitbitdata.xls', sheet_name='수면')
ActiveData = pd.read_excel('C:/Users/oyun/Desktop/fitbitdata.xls', sheet_name='활동')

print(type(ActiveData))
date = ActiveData['날짜']

kal = np.array(ActiveData['칼로리 소모량'])
for i in range(len(kal)):
    kal[i] = int(kal[i].replace(",",""))

step = np.array(ActiveData['걸음 수'])
for i in range(len(step)):
    step[i] = int(step[i].replace(",", ""))

distance = np.array(ActiveData['이동 거리'])

activetime = ActiveData['약간 활동적인 시간(분)']


# temp = ActiveData[['걸음 수', '칼로리 소모량']]
# print(temp.head())

a = np.array([[1,2,3,4]])
b = np.array([5,6,7,8])
print(b)

print(b.ndim)
print(b.shape)
b = b.reshape(1,-1)
print(b[b<8])
b = np.where(b<7, 100, 200)
print(b.shape)
print(b.ndim)
print(b)
print(b.flatten())
c = np.zeros(10,)
c = c+1
print(c)
# print(kal.dtype)
# print(distance.dtype)

def extract_date(column):
    return column.split(".")[2]

extractdate = date.apply(extract_date)

plt.subplot(2,2,1)
plt.plot(extractdate, kal)
plt.title("Calorie for Date")
plt.xlabel("Date")
plt.ylabel("Calorie")

plt.subplot(2,2,2)
plt.plot(extractdate, activetime)
plt.title("Active time for Date")
plt.xlabel("Date")
plt.ylabel("Active Time")

plt.subplot(2,2,3)
plt.plot(extractdate, step)
plt.title("Step for Date")
plt.xlabel("Date")
plt.ylabel("Steps")

plt.subplot(2,2,4)
plt.plot(extractdate, distance)
plt.title("Distance for Date")
plt.xlabel("Date")
plt.ylabel("Distance")
# plt.show()
