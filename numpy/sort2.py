import numpy as np

rng = np.random.default_rng(7)

# choice(set, sore_num ,replace =False ,p)
# 第一个参数是要抽样的集合，如果是一个整数，则表示从 0 到该值
# 第二个参数是样本大小
# 第三个参数表示结果是否可以重复
# 第四个参数表示出现的概率，长度和第一个参数一样
syc =rng.choice(4,2,replace=False,p=[.9,0,.1,0])
print(syc)
print("-------------------------")
syc_int = np.random.randint(0,50,(3,4))
syc_index1 = np.argmax(syc_int,axis=0)
syc_index2 = np.argmax(syc_int,axis=0)
print(syc_int)
print("-------------------------")
print(syc_index2)
print("-------------------------")