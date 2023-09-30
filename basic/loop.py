#range()函数，其中步长bu必须为整数，否则报错
#for	天然适合在有限的循环中
#while	可以被用在无限循环中
#break	紧急弹出
#continue	算了，我接着来
for i in range(5):  # 从0开始，到5结束，步长为1
    print("loop1.",str(i)+"新文件-" + str(i))
print("this is a new line")

for i in range(2,5) :   # 从2开始，到5结束，步长为1
    print("loop2.",str(i)+"循环2-" + str(i))
print("this is a new line")

for i in range(10,0,-3) :   # 从10开始，到0结束，步长为-3
    print("loop3.",str(i)+"循环3-" + str(i))
print("this is a new line")
guess_num = 18
while guess_num != 20:
    guess_num += 1
    print(guess_num)
print("this is a new line")
for i in range(10):
    if i % 2 == 0:
        continue    # 跳过偶数
    print(i)
print("this is a new line")
guess_num = 30
while guess_num != 25:
    guess_num += 1
    if guess_num > 25:
        print("guess_num > 25") 
        break   # 紧急弹出
    print(guess_num)