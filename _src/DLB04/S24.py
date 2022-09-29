import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
mpl.rcParams['axes.unicode_minus'] = False

x = np.arange(0, 2 * np.pi, 0.1)  # start,stop,step
y = np.cos(x)
plt.plot(x, y)
plt.show()
