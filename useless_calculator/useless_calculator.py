import math
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a,b):
        self.result = a + b
        return self.result

    def sub(self, a,b):
        self.result = a - b
        return self.result
    
    def mul(self, a,b):
        self.result = a * b
        return self.result
    
    def div(self, a,b):
        if b==0:
            print("被除数不能为0")
        else:
            self.result = a / b
            return self.result
    def add_list(self,list_a,list_b):
        if len(list_a) != len(list_b):
            print("两个列表长度不一致")
        else:
            res_list = []   # 定义一个空列表
            for i in range(len(list_a)):
                res_list.append(list_a[i] + list_b[i])  # 将两个列表对应位置的元素相加
        return res_list
    
    def sub_list(self,list_a,list_b):
        if len(list_a) != len(list_b):
            print("两个列表长度不一致")
        else:
            res_list = []   # 定义一个空列表
            for i in range(len(list_a)):
                res_list.append(list_a[i] - list_b[i])
        return res_list
    
    def mul_list(self,list_a,list_b):
        if len(list_a) != len(list_b):
            print("两个列表长度不一致")
        else:
            res_list = []
            for i in range(len(list_a)):
                res_list.append(list_a[i] * list_b[i])
        return res_list
    
    def entropy(self,list_a):
        res = 0
        for i in list_a:
            res += i * math.log(i,2)
        return -res
    
test_calculator = Calculator()
list_a = [0.1,0.2,0.3,0.4]
print(test_calculator.entropy(list_a))