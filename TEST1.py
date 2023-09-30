## 本段代码绘图使用无需理解
! pip3 install numpy matplotlib
import numpy as np
import matplotlib.pyplot as plt 
x = np.arange(0,5,0.1)
y = x
plt.plot(x,y)
y = x**2
plt.plot(x,y)
plt.xlabel('Imput size')
plt.ylabel('Running time')