# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:17:15 2020

@author: SAMED
"""

import math
import numpy as np

dosya= open('kapalipoligon.txt', mode="r")
satirlar=dosya.readlines()
dosya.close()
satirlar= [i.split(',') for i in satirlar] 

ss=len(satirlar)

A=np.zeros([ss,2])

for i in range (0,ss): 
    for j in range (0,2):
        A[i,j]=float(satirlar[i][j])
                                           
ka=A[:,0]
kenar=A[:,1]
kenar=np.delete(kenar, ss-1)

a0=float(input('Başlangıç semt açısını giriniz: '))
y0=float(input('Nirengi y koordinatı: '))
x0=float(input('Nirengi x koordinatı: '))

a=len(ka)
b=len(kenar)
aa=np.zeros([a,1])
aad=np.zeros([a,1])
dY=np.zeros([b,1])
dX=np.zeros([b,1])
for i in range(0,a):
    if i==0:
        aa[i]=a0+ka[i]
        if aa[i]<200:
            aa[i]=aa[i]+200
        elif aa[i]>=600:
            aa[i]=aa[i]-600
        else:
            aa[i]=aa[i]-200
    else:
        aa[i]=aa[i-1]+ka[i]
        if aa[i]<200:
            aa[i]=aa[i]+200
        elif aa[i]>=600:
            aa[i]=aa[i]-600
        else:
            aa[i]=aa[i]-200
t=a0+200
if t>400:
    t-=400
if t==aa[a-1]:
    pass
else:
    fB=aa[a-1]-t
    fBmax=0.015*(math.sqrt(b))
    if abs(fB)<fBmax:
        dhata=fB/a
    else:
        print('fB<fBmax sağlanmıyor açı kapanma hatası var') 
        
for j in range(0,a):
    dka=ka+(-dhata)
    if j==0:
        aad[j]=a0+dka[j]
        if aad[j]<200:
            aad[j]=aad[j]+200
        elif aad[j]>=600:
            aad[j]=aad[j]-600
        else:
            aad[j]=aad[j]-200
    else:
        aad[j]=aad[j-1]+dka[j]
        if aad[j]<200:
            aad[j]=aad[j]+200
        elif aad[j]>=600:
            aad[j]=aad[j]-600
        else:
            aad[j]=aad[j]-200
            
                      
            
for k in range(0,b):
     dY[k]=kenar[k]*math.sin(aad[k]*(math.pi/200))
     dX[k]=kenar[k]*math.cos(aad[k]*(math.pi/200))
dy=dY.sum()     
dx=dX.sum()
dk=kenar.sum()   
fs=math.sqrt(dy**2+dx**2)
fsmax=0.010*math.sqrt(dk)
dkhataY=np.zeros([b,1])
dkhataX=np.zeros([b,1])
if fs<fsmax:
    for dkhata in range(0,b):
        dkhataY[dkhata]=dy*kenar[dkhata]/dk
        dkhataX[dkhata]=dx*kenar[dkhata]/dk
    ddY=dY+(-dkhataY)
    ddX=dX+(-dkhataX)
else:
    print('fs<fsmax sağlanmıyor kaba kenar hatası var')
Y=np.zeros([b,1])
X=np.zeros([b,1])
for snc in range(0,b):
    if snc==0:
        Y[snc]=y0+ddY[snc]
        X[snc]=x0+ddX[snc]
    else:
        Y[snc]=Y[snc-1]+ddY[snc]
        X[snc]=X[snc-1]+ddX[snc]    
            
sonuc=np.array([Y,X])
sonuc=np.transpose(sonuc)
print('\n',sonuc)        


