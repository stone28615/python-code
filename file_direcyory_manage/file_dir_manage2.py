import os
import shutil # 文件操作模块

# 用户注销
if os.path.exists("user/syc"):
    os.removedirs("user/syc")
    print("syc用户注销成功")
else:
    print("syc用户不存在")