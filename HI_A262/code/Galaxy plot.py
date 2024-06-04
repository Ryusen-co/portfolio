# -*- coding: utf-8 -*-
# """
# Created on Tue Dec 27 14:05:57 2022

# @author: Hasif
# """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def deg2HMS(ra='', dec='', round=True):
  RA, DEC, rs, ds = '', '', '', ''
  if dec:
    if str(dec)[0] == '-':
      ds, dec = '-', abs(dec)
    deg = int(dec)
    decM = abs(int((dec-deg)*60))
    if round:
      decS = int((abs((dec-deg)*60)-decM)*60)
    else:
      decS = (abs((dec-deg)*60)-decM)*60
    DEC = '{0}{1}d {2}m {3}s'.format(ds, deg, decM, decS)
  
  if ra:
    if str(ra)[0] == '-':
      rs, ra = '-', abs(ra)
    raH = int(ra/15)
    raM = int(((ra/15)-raH)*60)
    if round:
      raS = int(((((ra/15)-raH)*60)-raM)*60)
    else:
      raS = ((((ra/15)-raH)*60)-raM)*60
    RA = '{0}{1}h {2}m {3}s'.format(rs, raH, raM, raS)
  
  if ra and dec:
    return (RA, DEC)
  else:
    return RA or DEC

df = pd.read_excel('Galaxy within 4500-5500 with Morphology.xlsx ', sheet_name='Spiral')
df2 = pd.read_excel('Galaxy within 4500-5500 with Morphology.xlsx', sheet_name='Elliptical')
df3 = pd.read_excel('Galaxy within 4500-5500 with Morphology.xlsx', sheet_name='Irregular etc')
df4 = pd.read_excel('Galaxy within 4500-5500 with Morphology.xlsx ', sheet_name='Lenticular')

S_RA = df['RA']
S_DEC = df['DEC']

E_RA = df2['RA']
E_DEC = df2['DEC']

x_cD = df2.at[0,'RA']
y_cD = df2.at[0, 'DEC']

L_RA = df4['RA']
L_DEC = df4['DEC']

I_RA = df3['RA']
I_DEC = df3['DEC']

figs, axs = plt.subplots(1, 1,figsize=(10,7), tight_layout = True)
figs.canvas.draw()

ytick=[0,35.25,32.50,35.75,36.00,36.25,36.50,36.75,37.00]
xtick=[0,27.0,27.5001,28.0,28.5001,29.0,29.5001]

for i in range(len(xtick)):
    xtick[i]= deg2HMS(ra=xtick[i])

for j in range(len(ytick)):
    ytick[j]=float(ytick[j])
    ytick[j]= deg2HMS(dec=ytick[j])

axs.set_yticklabels(ytick,rotation=15)
axs.set_xticklabels(xtick, rotation=15)
axs.scatter(S_RA,S_DEC, marker='o', label='Spiral', color='r')
axs.scatter(E_RA,E_DEC, marker='^', label= 'Elliptical', color='lime')
axs.scatter(L_RA,L_DEC, marker='*', label= 'Lenticular', color='gold',s=150)
axs.scatter(I_RA,I_DEC, marker='D', label= 'Irregular and N/A', color='b')
axs.scatter(x_cD,y_cD, marker='X', label='center Dominant',color='black', s=150)

font = {'family': 'Times New Roman','size':25}
#plt.title('Morphology and Position of various Galaxy-type in A262',fontdict=font,pad=20)
plt.xlabel('Right Ascension (RA)',fontsize=15)
plt.ylabel('Declination (DEC)',fontsize=15)

plt.legend()
plt.show()

