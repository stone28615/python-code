import numpy as np
rng = np.random.default_rng(42)

arr1 = rng.random((1, 3))
arr2 = rng.random((2, 3))
syc  = np.array([])
syc = syc.append(arr1[0])
print(syc)