import pandas as pd
import numpy as np

school_id_list = [{'name': 'John', 'job': "teacher", 'age': 40},
                {'name': 'Nate', 'job': "teacher", 'age': 35},
                {'name': 'Yuna', 'job': "teacher", 'age': 37},
                {'name': 'Abraham', 'job': "student", 'age': 10},
                {'name': 'Brian', 'job': "student", 'age': 12},
                {'name': 'Janny', 'job': "student", 'age': 11},
                {'name': 'Nate', 'job': "teacher", 'age': None},
                {'name': 'John', 'job': "student", 'age': None}
         ]
df = pd.DataFrame(school_id_list, columns = ['name', 'job', 'age'])

df['age'].fillna(df.groupby('job')['age'].transform('median'), inplace=True)
# print(df)

date_list = [{'yyyy-mm-dd': '2000-06-27'},
         {'yyyy-mm-dd': '2002-09-24'},
         {'yyyy-mm-dd': '2005-12-20'}]

df2 = pd.DataFrame(date_list, columns = ['yyyy-mm-dd'])

def extract_year(column):
    return column.split("-")[0]

def get_age(year, current_year):
    return current_year - int(year)

def get_introduce(age, prefix, suffix):
    return prefix + str(age) + suffix




df2['year'] = df2['yyyy-mm-dd'].apply(extract_year)
df2['age'] = df2['year'].apply(get_age, current_year=2018)

def get_inroduce2(row):
    return "I was born in "+str(row.year)+" my age is " + str(row.age)

df2['introduce2'] = df2.apply(get_inroduce2, axis=1)   # df2.introduce는 df2['introduce']와 동일하다.
df2['introduce'] = df2['age'].apply(get_introduce, prefix="I am ", suffix=" years old")
# print(df2)

date_list2 = [{'date': '2000-06-27'},
         {'date': '2002-09-24'},
         {'date': '2005-12-20'}]

df3 = pd.DataFrame(date_list2, columns=['date'])
df3['year'] = df3['date'].apply(extract_year)

# print(df3)

job_list = [{'age': 20, 'job': 'student'},
         {'age': 30, 'job': 'developer'},
         {'age': 30, 'job': 'teacher'}]
df4 = pd.DataFrame(job_list)
df4.job = df4.job.map({"student":1, "developer":2, "teacher":3})
# print(df4)

x_y = [{'x': 5.5, 'y': -5.6, 'z':-1.1},
         {'x': -5.2, 'y': 5.5, 'z':-2.2},
         {'x': -1.6, 'y': -4.5, 'z':-3.3}]
df5 = pd.DataFrame(x_y)
df5 = df5.applymap(np.around) #모든 컬럼에 적용하고 싶은 때는 applymap, 한 컬럼에 적용하고 싶을 때는 apply
print(df5)