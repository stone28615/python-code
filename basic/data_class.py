# List 列表
    # 在列表中，你可以存放不同类型的元素，字符，数字，甚至列表里还能有列表。
    # 列表是有序的，你可以通过索引来访问列表中的元素。
    # 列表是可变的，你可以在列表中添加，删除，修改元素。
    # 列表是可重复的，你可以在列表中添加重复的元素。
    # 列表是用[]来表示的，列表中的元素用逗号隔开。
    # 列表的索引是从0开始的。
    # 列表的切片是左闭右开的。
    # 列表的索引可以是负数，负数表示从右往左数。
    # 列表的切片可以省略开始索引，结束索引，步长。
file =[1,"文件2",["文件3",114514]]
print("line 1:",file[0],file[1],file[2])
print("line 2:",file[2][0],"这是中间的空白捏",file[2][1])
file[0] = "字符1"
print("line 3:",file[-1],file[-2],file[-3])
#-----------------------------------------------------这是一条分割线-----------------------------------------------------
# Dict 字典
    # 字典是无序的，你不能通过索引来访问字典中的元素。
    # 字典是可变的，你可以在字典中添加，删除，修改元素。
    # 字典是可重复的，你可以在字典中添加重复的元素。
    # 字典是用{}来表示的，字典中的元素用逗号隔开。
    # 字典的索引是键值对。
    # 字典的切片是左闭右开的。
    # 字典的索引可以是负数，负数表示从右往左数。
    # 字典的切片可以省略开始索引，结束索引，步长。
Dict_file ={"字典1":730,"字典2":129,"字典3":"文件3"}
print("line 4:",Dict_file["字典1"],Dict_file["字典2"],Dict_file["字典3"])

#-----------------------------------------------------这是一条分割线-----------------------------------------------------
print("this is a new line")
# Set 集合  集合概念与数学中的集合概念一致
    # 集合是无序的，你不能通过索引来访问集合中的元素。
    # 集合是可变的，你可以在集合中添加，删除元素。
    # 集合是不可重复的，你不能在集合中添加重复的元素。
    # 集合是用{}来表示的，集合中的元素用逗号隔开。
    # 集合的索引是从0开始的。
    # 集合的切片是左闭右开的。
    # 集合的索引可以是负数，负数表示从右往左数。
    # 集合的切片可以省略开始索引，结束索引，步长。
Set_file ={"集合1","集合2","集合3","集合1"}
print("line 6:",Set_file)
#-----------------------------------------------------这是一条分割线-----------------------------------------------------
print("this is a new line")
# Tuple 元组  元组一般很少使用
    # 元组是有序的，你可以通过索引来访问元组中的元素。
    # 元组是不可变的，你不能在元组中添加，删除，修改元素。
    # 元组是可重复的，你可以在元组中添加重复的元素。
    # 元组是用()来表示的，元组中的元素用逗号隔开。
    # 元组的索引是从0开始的。
    # 元组的切片是左闭右开的。
    # 元组的索引可以是负数，负数表示从右往左数。
    # 元组的切片可以省略开始索引，结束索引，步长。
Tuple_file =("元组1","元组2","元组3")
print("line last1:",Tuple_file[0],Tuple_file[1],Tuple_file[2])
print("line last2:",Tuple_file[-1],Tuple_file[-2],Tuple_file[-3])