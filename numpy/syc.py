import numpy as np
print (np.arange(15).reshape(3, 5))
print (np.array([1,2,3]))
syc_array = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print("\nsyc_array: ", syc_array, "\nsyc_array.shape: ", syc_array.shape, 
      "\nsyc_array.ndim: ", syc_array.ndim, 
      "\nsyc_array.dtype.name: ", syc_array.dtype.name, 
      "\nsyc_array.itemsize: ", syc_array.itemsize, 
      "\nsyc_array.size: ", syc_array.size,
      "\nsyc_shape[0]:", syc_array.shape[0],         
      "\ntype(syc_array): ", type(syc_array))
