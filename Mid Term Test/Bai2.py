# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 13:18:58 2024

@author: SinhVien
"""

from matplotlib import pyplot as plt


population = [59.69, 16, 9.94, 7.79, 5.68, 8.54]
country = ['Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia']


plt.pie(population, labels=country,colors=colors, autopct='%1.2f',startangle=90)

plt.show()