# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frency=10 # 载波频率>2/T
T=1       # 符号持续时间
fs=30     # fs>2*(frency+B)   B为基带信号宽带
t=np.linspace(1,100,1000)

x=np.linspace(1,100,1000)
sinGama=np.pi*2*frency*t


fig,ax=plt.subplots()

ax.set_xlim(0,10)
ax.set_ylim(0,10)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# 添加辅助线
ax.axhline(0, color='black', alpha=0.5, lw=0.5)  # 水平参考线
ax.axvline(0, color='black', alpha=0.5, lw=0.5)  # 垂直参考线

# 添加网格和标题
ax.grid(True, linestyle='--', alpha=0.6)
plt.show()