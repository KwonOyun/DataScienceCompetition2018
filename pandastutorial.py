import pandas as pd

data_frame = pd.read_csv("C:/Users/oyun/Desktop/test.csv")
s1 = pd.core.series.Series([1,2,3])
s2 = pd.core.series.Series(['one', 'two', 'three'])
temp = pd.DataFrame(data=dict(num=s1, word=s2))
print(temp)