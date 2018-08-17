import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):

    return np.arange(n**2).reshape(n,n)


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type==0:
        return np.zeros(shape=shape, dtype=dtype)
    if type==1:
        return np.ones(shape=shape, dtype=dtype)
    if type==99:
        return np.empty(shape=shape, dtype=dtype)


def change_shape_of_ndarray(X, n_row):
    return X.flatten() if n_row==1 else X.reshape(n_row,-1)

def concat_ndarray(X_1, X_2, axis):
    try:
        if X_1.ndim == 1:
            X_1 = X_1.reshape(1, -1)
        if X_2.ndim == 1:
            X_2 = X_2.reshape(1, -1)
        return np.concatenate((X_1,X_2), axis=axis)
    except ValueError as e:
        return False


def normalize_ndarray(X, axis=99, dtype=np.float32):

    return


def save_ndarray(X, filename="test.npy"):
    pass


def boolean_index(X, condition):
    pass


def find_nearest_value(X, target_value):
    pass


def get_n_largest_values(X, n):
    pass

# print(n_ize_ndarray_creation(3))
# # print(zero_or_one_or_empty_ndarray((2,2),99))s
# test_array = np.arange(32).reshape(4,8)
# print(test_array)
# print(change_shape_of_ndarray(test_array,8))
a = np.array([[1,2], [3,4]])
b = np.array([[5,6],[7,8]])
print(a.flatten())

print(concat_ndarray(a,b,1))