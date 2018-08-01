import numpy as np

test_array = np.arange(9).reshape(3,3)
# print(test_array.reshape(-1, 3))
array2 = np.zeros(shape=(3,4), dtype=np.int8)
# print(array2)
array3 = np.zeros((5,6))
np.ones_like(array3)
# print(np.ones_like(array3))
# print(np.diag(test_array, k=1))
# print(np.random.uniform(0,2,8).reshape(2,4))
# print(test_array)
# print(test_array.sum(axis=0))
test_array2 = np.arange(10,19).reshape(3,3)
# print(test_array2)
# print(test_array.transpose())
# print(test_array**2)

kwon = [[4,3,2],[2,3,4],[1,3,2]]
# print(kwon)
kwonnp = np.array(kwon)
print(kwonnp)
B = kwonnp>2
print(B)