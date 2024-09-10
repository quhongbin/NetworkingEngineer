import matplotlib.pyplot as plt
import numpy as np

#定义域取值
x_values=np.arange(0,450.1,1) #endpoint表示不包含末尾值
x=x_values*(np.pi/180)  #转换为弧度制
# y1=np.sin(x-(np.pi/2))
y=np.sin(x)
fig=plt.figure(figsize=([16,8]))

#制作标签
#radian=np.arange(0,450,90)
#radian_ticks=[r'$0$',r'$\frac{\pi}{2}$',r'$\pi$',r'$\frac{3\pi}{2}$',r'$2\pi$']
#设置标签
# ax[0,0].set_xticks(radian)
# ax[0,0].set_xticklabels(radian_ticks)
#####   sin(x)  #####
plt.plot(x_values,y,label=r"$sin(x)$")
#####  3sin(x) #####
plt.plot(x_values,y*3,label=r"$3sin(x)$ 振幅")
##### sin(x-pi/2) #####
y_phase=np.sin(x-(np.pi/2))
plt.plot(x_values,y_phase,label=r"$\sin(x+\frac{\pi}{2})$ 相位")
#####   sin(1/2*x)  #####
x_values_frequent=np.arange(0,900.1,1)
y_frequent=np.sin(x_values_frequent*(np.pi/180))
plt.plot(1/2*x_values_frequent,y_frequent,label=r"$\sin(\frac{1}{2}x)$ 频率")

#####   3sin(1/2x+pi/2)   #####
# x_values_zhonghe=np.arange(0,1080.1,1)
# y_zhonghe=np.sin(x_values_zhonghe*(np.pi/180)-np.pi/2)
# plt.plot(1/2*x_values_zhonghe,3*y_zhonghe,label=r"$3\sin(\frac{1}{2}x+\frac{\pi}{2})$")

#设置网格
plt.grid(which='major',linestyle="-",alpha=0.9)
plt.grid(which="minor",linestyle=":",color="gray",alpha=0.5)
plt.xticks(np.arange(0,450,90)) #设置标签
plt.legend() #显示label

# plt.plot(x_values,y1,linestyle=":",label="相位0.5)
plt.rcParams['font.sans-serif']=['SimHei'] #显示支持中文
plt.rcParams['axes.unicode_minus']=False
plt.show()
