# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:36:18 2020

@author: SAMED
"""

# dosya=open('açikpoligon.txt', mode="r")
import math
import numpy as np

A= np.loadtxt("acikpoligon.txt", dtype='f', delimiter=' ')
                                                 
a0=float(input('Başlangıç semt asçısını giriniz: '))
y0=float(input('Nirengi y koordinatı: '))
x0=float(input('Nirengi x koordinatı: '))

# A=np.array([(157.6210,201.35),(224.4125,193.67),(173.7340,204.32)])
a=len(A)
alf=np.zeros([a,1])
Y=np.zeros([a,1])
X=np.zeros([a,1])
for i in range(0,a):
    if i==0:
        alf[i,0]=a0+A[i,0]
        if alf[i,0]<200:
            alf[i,0]=alf[i,0]+200
        elif alf[i,0]>=600:
            alf[i,0]=alf[i,0]-600
        else:
            alf[i,0]=alf[i,0]-200
        Y[i,0]=y0+A[i,1]*math.sin(alf[i,0]*(math.pi/200))
        X[i,0]=x0+A[i,1]*math.cos(alf[i,0]*(math.pi/200))
    else:
        alf[i,0]=alf[i-1,0]+A[i,0]
        if alf[i,0]<200:
            alf[i,0]=alf[i,0]+200
        elif alf[i,0]>=600:
            alf[i,0]=alf[i,0]-600
        else:
            alf[i,0]=alf[i,0]-200
        Y[i,0]=Y[i-1,0]+A[i,1]*math.sin(alf[i,0]*(math.pi/200))
        X[i,0]=X[i-1,0]+A[i,1]*math.cos(alf[i,0]*(math.pi/200))
snc=np.array([Y,X])
snc=np.transpose(snc)
print('\n',snc)
