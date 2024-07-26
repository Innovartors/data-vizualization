#Ho ten: Dau Hong Phuc
#mssv: 2100006214

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np


np.random.seed(19680813)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

colors = ['c', 'g', 'm', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    # random gia tri mang tren truc x va truc y
    xs = np.arange(40)
    ys = np.random.rand(40)

   
    cs = [c] * len(xs)
    cs[0] = 'c'

    
    ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

#set yticks cho bieu do ax
ax.set_yticks(yticks)

plt.show()
