# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:02:47 2024

@author: SinhVien
"""

import matplotlib.pyplot as plt


y = [1, 4, 9, 16, 25, 36, 49, 64]
lt = [1, 26, 40, 50, 65, 68, 87, 98]
dt = [1,6,12,18,28, 40, 52, 65]

plt.plot(lt, y, 'y-', marker='s', label='Laptop')

plt.plot(dt, y, 'g--', marker='o', label='Dien thoai')

plt.title("Chi so ban hang")
plt.xlabel("Thoi gian")
plt.ylabel("So luong ban")

plt.legend(loc='lower right')

plt.grid(True)
plt.show()