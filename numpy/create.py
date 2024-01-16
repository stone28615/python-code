import numpy as np
syc = np.arange(6).reshape(2,3) #reshape中的元素数量要与原始的数量相同
print(syc)
syc_linspace = np.linspace(0,7,5)# （begin ，end ,total_number）
print(syc_linspace)
syc_logspace = np.logspace(0,9,6,base=2).reshape(2,3)
print(syc_logspace)

#使用random生成
syc_rng_int = np.random.randint(0,9,(2,3))
syc_rng_uniform = np.random.uniform(0,10,(3,3))#离散均匀分布
syc_rng_normal = np.random.normal(3,1,(3,4))#正态分布
print(syc_rng_normal.shape)
print(syc_rng_int)