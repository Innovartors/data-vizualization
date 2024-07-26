# -*- coding: utf-8 -*-
"""2100008197_PhanChiHieu_Lab1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1THZoXqDHQE71m7ylum7snNLwpohhXJw4
"""



"""1.	Vẽ biểu đồ Line nét chấm dotted và có màu xanh"""

import matplotlib.pyplot as plt
import numpy as np

x_points_2=np.array([1.2,3,6,9,14.5])
y_points_2=np.array([10,9,22,15,50])

plt.plot(x_points_2,y_points_2,linestyle='dotted',c='g')
plt.show();

"""2.	Kết hợp vẽ 2 Lines để hiển thị kết quả sau:"""

import matplotlib.pyplot as plt
import numpy as np

x_points_2=np.array([1.2,3,6,9,14.5])
y_points_2=np.array([10,9,22,15,50])
x_points = np.array([1.2,3,7,13])
y_points = np.array([9.2,23,15,45])
plt.plot(x_points,y_points,'r--')
plt.plot(x_points_2,y_points_2,linestyle='dotted',c='g')
plt.show();

"""3.	Vẽ Line có đỉnh hình vuông và nét dứt màu đỏ hiển thị kết quả sau:"""

import matplotlib.pyplot as plt
import numpy as np
x_points_1=np.array([1,2,3,5,7])
y_points_1=np.array([5,2,5,20,10])
plt.plot(x_points_1,y_points_1,'rD--')
plt.show();

"""4.	Vẽ biểu đồ sau để hiển thị sự tăng giảm của Giá nhiên liệu trong năm 2020:


"""

import matplotlib.pyplot as plt
import numpy as np
x = np.array([20,22,24,26,28,30])
y_points_1 = np.array([5,3,5,4,4.8,4.8])
y_points_2 = np.array([4,4.5,5,3,4,7])
y_points_3 = np.array([5,4,6,4,6,8])
plt.plot(x, y_points_1,'b', label="Xăng")
plt.plot(x,y_points_2,'g', label="Dầu")
plt.plot(x,y_points_3,'r', label="Nhớt" )
plt.legend()
plt.xlabel("Giá nhiên liệu (VNĐ)")
plt.ylabel("Biểu đồ nhiên liệu trong nước (năm 2020)")
plt.show()
