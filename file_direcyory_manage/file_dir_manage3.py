import os
import shutil # 文件操作模块

# 用户注销若是目录下有文件则无法注销
os.makedirs("user/syc", exist_ok=True)
with open("user/syc/hello.txt", "w") as f:
    f.write("hello")
#os.removedirs("user/syc")   # OSError: [Errno 39] Directory not empty: 'user/syc'
shutil.rmtree("user/syc")   # 删除目录下所有文件
print(os.listdir("user"))
