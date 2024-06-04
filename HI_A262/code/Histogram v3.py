# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 15:45:22 2023

@author: Fyrel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from fitter import Fitter
from scipy.optimize import curve_fit


df = pd.read_csv('Binning data A262 (1).csv')
df2 = pd.read_excel('Galaxy within 4500-5500 with Morphology.xlsx', sheet_name='histo2')

v=df2['Velocity, V']


x = df['velocity']
y = df['Average of antenna temp (K)']

velocity = x.values

def Gauss(x, a, miu, sigma):
    return a * np.exp(((-(x-miu)**2)/(2*sigma**2)))

def func(x, a1, a2, a3, miu1, miu2, miu3, sigma1, sigma2, sigma3):
    return Gauss(x, a1, miu1, sigma1)+ Gauss(x, a2, miu2, sigma2)+Gauss(x, a3, miu3, sigma3)

# a=[0.11,1.28,0.22]
# miu=[4740,5000,5200]
# sigma=[2,2,2]
    
a=np.max(y)
miu=x[np.argmax(y)]
# sigma=np.std(x)  
sigma = 1000

print(a, miu, sigma)

newparam, _ = curve_fit(Gauss,x,y, p0=[a,miu,sigma])

# bestparam, _ = curve_fit(func, x, y, p0=[*a, *miu, *sigma]) #* pecahkan ikut urutan
# 
# print([*a, *miu, *sigma])
# print(bestparam)
print(newparam)
y_fit = Gauss(x, a, miu, newparam[-1])

# y_fit=Gauss(x,a,x[miu],sigma)


x = np.asarray(x)
y = np.asarray(y)

# y=y*6
# y_fit=y_fit*6
n_bins=[4500,4600,4700,4800,4900,5000,5100,5200,5300,5400,5500]
figs, axs = plt.subplots(1, 1,figsize=(10,7), tight_layout = True)

ytick=[0,'',0.2,'',0.4,'',0.6,'',0.8,'',1.0,'',1.2]
#n, bins, patches = axs.hist(v, bins=n_bins,alpha=0.5)
axs.grid(visible=False, color='black', linestyle='--',linewidth = 0.5)

axs.plot(x,y, color='black', marker='o', linestyle=':', label='Scale of temperature data')
axs.plot(x,y_fit,color='orange',label='Gaussian Fitting')
axs.set_yticklabels(ytick)
plt.xticks(np.arange(4500,5600,100))
plt.yticks(np.arange(0,1.3,0.1))
font = {'family': 'Times New Roman','size':25}
plt.title('Histogram of no. of galaxy within certain velocity',fontdict=font,pad=20)
plt.ylabel('Number of galaxy',fontsize=15)
plt.xlabel('Velocity (km/s)',fontsize=15)
plt.legend()
plt.show()