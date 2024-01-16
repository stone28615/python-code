# 数据集
from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()  # 加载数据集
data = iris["data"] # 获取特征向量
target = iris["target"] # 获取标签

# Sigmoid
def sigmoid(x: np.array, derive: bool = False) -> np.array:
    if derive:
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))
#print(target)

def predict(x,w):
    return sigmoid(x.dot(w))

batch_size = 5
test_size = int(target.size*0.2)
test_index = [2+5*i for i in range(test_size)]
data_indedx = [i for i in range(target.size) if i not in test_index] 
test_set = data[test_index]
data_set = data[data_indedx]
