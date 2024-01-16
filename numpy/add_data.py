import numpy as np

syc1 = np.random.randint(0,9,(2,4))
syc2 = np.random.randint(0,9,(2,2))
syc_concatenate = np.concatenate((syc1,syc2),axis=1) #axis默认为0，axis=0 表示从上往下拼接，axis=1表示水平拼接 ，for 2D data
syc_split = np.split(syc_concatenate,3,axis=1)

print (syc1)
print("-------------------")
print(syc2)
print("-------------------")
print(syc_concatenate)
print("-------------------")
print(syc_split[0])
