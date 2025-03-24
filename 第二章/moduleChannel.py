import matplotlib.pyplot as plt
import numpy as np

# 创建数据示例（正态分布）
x=np.linspace(1,100,1000)
 # 生成X轴数据
 # 生成Y轴数据



# 根据象限分配颜色（自定义颜色映射）
# colors = []
# for xi, yi in zip(x, y):
#     if xi >= 0 and yi >= 0:
#         colors.append('red')    # 第一象限
#     elif xi < 0 and yi >= 0:
#         colors.append('blue')   # 第二象限
#     elif xi < 0 and yi < 0:
#         colors.append('green')  # 第三象限
#     else:
#         colors.append('purple')# 第四象限

# 创建画布和坐标轴
fig, ax = plt.subplots(figsize=(8, 8))

# 绘制散点图
# scatter = ax.scatter(x, y, c=colors, alpha=0.6, edgecolors='w')

# 设置坐标轴样式
# ax.spines['left'].set_position('center')     # 将左侧轴线移动到零位置
# ax.spines['bottom'].set_position('center')   # 将底部轴线移动到零位置
ax.spines['right'].set_visible(False)      # 隐藏右侧轴线
ax.spines['top'].set_visible(False)       # 隐藏顶部轴线

# 添加辅助线
ax.axhline(0, color='black', alpha=0.5, lw=0.5)  # 水平参考线
ax.axvline(0, color='black', alpha=0.5, lw=0.5)  # 垂直参考线

# 设置坐标轴范围和标签
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_xlabel('X Axis', loc='right')  # X轴标签放在右侧
ax.set_ylabel('Y Axis', loc='top')    # Y轴标签放在顶部

# 添加象限标签
# ax.text(3, 3, 'Q1', ha='center', va='center', fontsize=20, alpha=0.3)
# ax.text(-3, 3, 'Q2', ha='center', va='center', fontsize=20, alpha=0.3)
# ax.text(-3, -3, 'Q3', ha='center', va='center', fontsize=20, alpha=0.3)
# ax.text(3, -3, 'Q4', ha='center', va='center', fontsize=20, alpha=0.3)

# 添加图例说明
# legend_labels = {
#     'red': 'Positive X & Y',
#     'blue': 'Negative X, Positive Y',
#     'green': 'Negative X & Y',
#     'purple': 'Positive X, Negative Y'
# }
# handles = [plt.Line2D([0], [0], marker='o', color='w', 
#                       markerfacecolor=color, markersize=10)
#            for color in legend_labels.keys()]
# ax.legend(handles, legend_labels.values(), 
#          title='Quadrant Legend', 
#          loc='upper right',
#          frameon=True)

# 添加网格和标题
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title('Quadrant Chart Example', pad=20)

plt.tight_layout()
plt.show()