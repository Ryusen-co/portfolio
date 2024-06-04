# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:19:29 2022

@author: Fyrel
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('c:/Users/Fyrel/Desktop/FYP/Data/Binning data A262 (1).csv')
df2 = pd.read_csv('c:/Users/Fyrel/Desktop/FYP/Data/Galaxy within 4500-5500.csv')
yerr = pd.read_csv('c:/Users/Fyrel/Desktop/FYP/Data/Error of the binned A262.csv')

figs, axs = plt.subplots(1, 1,figsize=(10,7), tight_layout = True)

x = list(df['Average (km/s)'])
y = list(df['Average of antenna temp (K)'])
yerr = list(df['Average of every 32 channels'])

x = np.asarray(x)
y = np.asarray(y)
y_err = np.asarray(yerr)


axs.errorbar(x,y, yerr=y_err,color='black', marker='o', linestyle=':', elinewidth=0.5, capsize=2)
plt.xticks(np.arange(4500,5600,100))
font = {'family': 'Times New Roman','size':25}
plt.title('',fontdict=font,pad=20)
plt.ylabel('Antenna temperature (K)',fontsize=15)
plt.xlabel('Velocity (km/s)',fontsize=15)
plt.show()