import pandas as pd
import numpy as np

data_frame = pd.read_csv("C:/Users/oyun/Desktop/test.csv")
# print(data_frame.head(3))

friend_dict_list = [
    {'name' : 'John', 'age' : 15, 'midterm' : 67 , 'final' : 80,'job' : 'student'},
    {'name' : 'Nate', 'age' : 26,'midterm' : 87 , 'final' : 95,'job' : 'teacher'},
    {'name' : 'Jenny', 'age' : 23,'midterm' : 84 , 'final' : 87,'job' : 'Soccer'}
]

df1 = pd.DataFrame.from_dict(friend_dict_list)
df1 = df1[['name', 'age', 'job']]
df1 = df1.drop('age', axis=1)
# print(df1)

df2 = pd.DataFrame.from_dict(friend_dict_list)
df2 = df2[['name', 'midterm', 'final']]
# df2['salary'] = np.where(df2['job'] != 'student', 'yes', 'no')
df2['total'] = df2['midterm'] + df2['final']
df2['average'] = df2['total']/2
grades = []
for row in df2['average'] :
    if row>=90:
        grades.append('A')
    elif row>=80:
        grades.append('B')
    else :
        grades.append('F')

df2['grade'] = grades
print(df2)

# print(df.head())
# df.to_csv("C:/Users/oyun/Desktop/test1.csv")

friend_list = [
    ['name', ['John', 'Jenny', 'Nate']],
    ['age', [20,30,30]],
    ['job', ['student', 'develop', 'teacher']]
]
# df = pd.DataFrame.from_items(friend_list)
# print(df.iloc[:2,0:3])
# df_filtered = df[['name', 'age']]
# print(df_filtered)
# df_filtered2 = df.filter(items=['age', 'job'])
# print(df_filtered2)
# df_filtered3 = df.filter(like='a', axis=1)
# print(df_filtered3)
# df_filtered4 = df.filter(regex='b$', axis=1)
# print(df_filtered4)
