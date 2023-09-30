import os
import shutil # 文件操作模块

# 修改用户姓名
os.makedirs("user/syc", exist_ok=True)
os.rename("user/syc", "user/BrushStone")