import numpy as np
a = np.array([[1, 2, 3]], dtype='int16')
b = np.array([[1, 2, 3], [4, 5, 6]], dtype='int32')
print(a.shape)
print(b.shape)
print(a.itemsize)
print(b.itemsize)