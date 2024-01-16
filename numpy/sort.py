import numpy as np
b = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
])


condition = (b > 2) & (b < 11)
b_condition =b[condition]
b_where = np.where(condition , b ,'NaN')

print("condition:\n", condition)
print("b[condition]:\n", b[condition])

print(b_where)#b中不符合（b<5）条件的全部变为0
print(b)
