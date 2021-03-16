# -*- coding='utf-8' -*-

from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
# plt.style.use('classic')
import datetime

CN_el_data = []
with open('US_EL.txt', 'r') as f:
    for line in f:
        if line != '':
            CN_el_data.append(float(line))

breakout_point = [0, 39, 144, 315]

ind = list(range(len(CN_el_data)))
plt.plot(ind, CN_el_data, color='gray')
for i in range(1, len(breakout_point)-1):
    plt.plot([breakout_point[i]]*2, [-0.5, 0.5], color='red', linestyle='--', linewidth=1)
plt.show()

titles = ['Period 1', 'Period 2', 'Period 3']
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
for i in range(len(breakout_point)-1):
    ax = plt.subplot(1, 3, i+1)
    temp_el_data = []
    for j in range(breakout_point[i], breakout_point[i+1]):
        temp_el_data.append(CN_el_data[j])
    if i == 4:
        temp_el_data.remove(min(temp_el_data))
    if i == 5:
        temp_el_data.remove(max(temp_el_data))
    print('length:', len(temp_el_data))
    print('KS_test:', stats.kstest(temp_el_data, 'norm'))
    print('SW_test:', stats.shapiro(temp_el_data))
    tuple, res = stats.probplot(temp_el_data, dist='norm', plot=plt)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.title(titles[i], fontdict={'color': 'black', 'size':18, 'family':'Times New Roman'})
    plt.xlabel('Theoretical quantiles', fontdict={'color': 'black', 'size':16, 'family':'Times New Roman'})
    plt.ylabel('Ordered Values', fontdict={'color': 'black', 'size':16, 'family':'Times New Roman'})
    print('slop, intercept, r:', res)
    print('*********************************************************')
plt.tight_layout()
plt.show()