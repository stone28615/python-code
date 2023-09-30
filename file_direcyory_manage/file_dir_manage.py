import os
import shutil # 文件操作模块
# 用户注册
if os.path.exists("user/syc"):
    print("syc用户已存在")
else:
    os.makedirs("user/syc", exist_ok=True)
    print("syc用户创建成功")
print(os.listdir("user"))
