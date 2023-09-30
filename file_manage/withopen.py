# with open ("loveletter.txt","r") as f:
# w : write
# r : read
# a : append
# w+ : write and read
# r+ : read and write
# a+ : append and read
# x : create
with open("new_file.txt", "r") as f:
    print(f.read())
with open("new_file.txt", "r+") as f:
    f.write("text has been replaced")
    f.seek(0)       # 将开始读的位置从写入的最后位置调到开头
    print(f.read())

with open("new_file.txt", "a+") as f:
    print(f.read())
    f.write("\nadd new line")
    f.seek(0)       # 将开始读的位置从写入的最后位置调到开头
    print(f.read())
