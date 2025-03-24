import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle

# 参数设置
fc = 10  # 载波频率（Hz）
T = 1    # 每个比特持续时间（秒）
fs = 100 # 采样率（Hz）
bits = [1, 0, 1, 1, 0]  # 数字信号序列
num_bits = len(bits)
total_time = num_bits * T
t = np.linspace(0, total_time, num_bits * T * fs, endpoint=False)

# 生成数字信号波形
bit_indices = np.floor(t / T).astype(int)
digital_wave = np.array([bits[i] if i < len(bits) else bits[-1] for i in bit_indices])

# 生成调制信号
carrier = np.sin(2 * np.pi * fc * t)

# 幅度键控（ASK）
ask_signal = digital_wave * carrier

# 相位键控（PSK）
phase = np.pi * digital_wave  # 0或π相位
psk_signal = np.sin(2 * np.pi * fc * t + phase)

# 频率键控（FSK）
f1, f2 = 5, 15  # 两个不同频率
fsk_signal = np.zeros_like(t)
for i in range(num_bits):
    start = i * T * fs
    end = (i+1) * T * fs
    bit = bits[i]
    freq = f1 if bit == 0 else f2
    t_segment = t[start:end] - i*T  # 时间从0到T每个比特
    fsk_signal[start:end] = np.sin(2 * np.pi * freq * t_segment)

# 创建图形和子图
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
fig.subplots_adjust(hspace=0.5)

# 初始化图形设置
y_pos = 1.2  # 数字信号显示位置
height = 0.2  # 数字信号矩形高度

for ax in (ax1, ax2, ax3):
    ax.set_xlim(0, total_time)
    ax.set_ylim(-1.7, 1.7)
    ax.grid(True)

ax1.set_title('Amplitude Shift Keying (ASK)', fontsize=10)
ax2.set_title('Phase Shift Keying (PSK)', fontsize=10)
ax3.set_title('Frequency Shift Keying (FSK)', fontsize=10)

# 创建数字信号矩形块
rects_ask, rects_psk, rects_fsk = [], [], []
for i, bit in enumerate(bits):
    color = 'green' if bit == 1 else 'red'
    
    rect_ask = Rectangle((i*T, y_pos), T, height, alpha=0.5, 
                        facecolor=color, edgecolor='black')
    rect_psk = Rectangle((i*T, y_pos), T, height, alpha=0.5, 
                        facecolor=color, edgecolor='black')
    rect_fsk = Rectangle((i*T, y_pos), T, height, alpha=0.5, 
                        facecolor=color, edgecolor='black')
    
    for rect in [rect_ask, rect_psk, rect_fsk]:
        rect.set_visible(False)
    
    ax1.add_patch(rect_ask)
    ax2.add_patch(rect_psk)
    ax3.add_patch(rect_fsk)
    
    rects_ask.append(rect_ask)
    rects_psk.append(rect_psk)
    rects_fsk.append(rect_fsk)

# 初始化调制信号线条
line_ask, = ax1.plot([], [], 'b', lw=1, label='Modulated Signal')
line_psk, = ax2.plot([], [], 'b', lw=1, label='Modulated Signal')
line_fsk, = ax3.plot([], [], 'b', lw=1, label='Modulated Signal')

# 添加图例
for ax in (ax1, ax2, ax3):
    ax.plot([], [], color='green', alpha=0.5, label='Bit=1')
    ax.plot([], [], color='red', alpha=0.5, label='Bit=0')
    ax.legend(loc='upper right')

def init():
    for line in [line_ask, line_psk, line_fsk]:
        line.set_data([], [])
    return line_ask, line_psk, line_fsk

def update(frame):
    current_time = (frame + 1) * T
    current_index = int(current_time * fs)
    
    # 显示当前比特的数字信号矩形
    for i in range(frame + 1):
        if i < len(rects_ask):
            rects_ask[i].set_visible(True)
            rects_psk[i].set_visible(True)
            rects_fsk[i].set_visible(True)
    
    # 更新调制信号数据
    x = t[:current_index]
    line_ask.set_data(x, ask_signal[:current_index])
    line_psk.set_data(x, psk_signal[:current_index])
    line_fsk.set_data(x, fsk_signal[:current_index])
    
    # 滚动显示最新3个比特
    for ax in (ax1, ax2, ax3):
        ax.set_xlim(max(0, current_time - 3), min(total_time, current_time + 1))
    
    return line_ask, line_psk, line_fsk, *rects_ask, *rects_psk, *rects_fsk

# 创建动画
ani = FuncAnimation(fig, update, frames=num_bits,
                    init_func=init, blit=True, interval=T*1000, repeat=False)

plt.show()