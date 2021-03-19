# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 09:03:13 2019

@author: SAMED
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:21:24 2019

@author: SAMED
"""


import math 
import numpy as np

dosya= open('dayalipoligon.txt', mode="r")
satirlar=dosya.readlines()
dosya.close()
satirlar= [i.split(' ') for i in satirlar] 

ss=len(satirlar)

A=np.zeros([ss,2])

for i in range (0,ss): 
    for j in range (0,2):
        A[i,j]=float(satirlar[i][j])
                                           
ka=A[:,0]
kenar=A[:,1]
kenar=np.delete(kenar, ss-1)

a0=float(input('Başlangıç semt açısını giriniz: '))
a1=float(input('Son semt açısını giriniz: '))
y0=float(input('İlk Nirengi y koordinatı: '))
x0=float(input('İlk Nirengi x koordinatı: '))
y1=float(input('Son Nirengi y koordinatı: '))
x1=float(input('Son Nirengi x koordinatı: '))

a=len(ka)
b=len(kenar)
aa=np.zeros([a,1])
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

if a1==aa[a-1]:
    pass
else:
    fB=aa[a-1]-a1
    fBmax=0.015*(math.sqrt(b))
    if abs(fB)<fBmax:
        dhata=fB/a
    else:
        print('fB<fBmax sağlanmıyor açı kapanma hatası var')  
for j in range(0,a):
    dka=ka+(-dhata)
    if j==0:
        aa[j]=a0+dka[j]
        if aa[j]<200:
            aa[j]=aa[j]+200
        elif aa[j]>=600:
            aa[j]=aa[j]-600
        else:
            aa[j]=aa[j]-200
    else:
        aa[j]=aa[j-1]+dka[j]
        if aa[j]<200:
            aa[j]=aa[j]+200
        elif aa[j]>=600:
            aa[j]=aa[j]-600
        else:
            aa[j]=aa[j]-200
for k in range(0,b):
     dY[k]=kenar[k]*math.sin(aa[k]*(math.pi/200))
     dX[k]=kenar[k]*math.cos(aa[k]*(math.pi/200))
     
     
     
#     BURASI DEĞİŞİCEK
dy=dY.sum()     
dx=dX.sum()
dk=kenar.sum()  
fy=dy-(y1-y0)
fx=dx-(x1-x0)
S=math.sqrt(dy**2+dx**2)



fQ=(1/dk)*((fy*dx)-(fx*dy))
fL=(1/dk)*((fy*dy)+(fx*dx))
fQmax=0.05+0.15*math.sqrt(S/1000)
fLmax=0.05+0.04*math.sqrt(a-1)
if fQ<fQmax:
    pass
else:
    print('fQ : Enine kapanma hatası; açılardan kaynaklanan hata')
if fL<fLmax:
    pass
else:
    print('fL : Boyuna kapanma hatası; uzunluktan kaynaklanan hata')

dkhataY=np.zeros([b,1])
dkhataX=np.zeros([b,1])
for dkhata in range(0,b):
    dkhataY[dkhata]=fy*kenar[dkhata]/dk
    dkhataX[dkhata]=fx*kenar[dkhata]/dk
dY=dY+(-dkhataY)
dX=dX+(-dkhataX)

Y=np.zeros([b,1])
X=np.zeros([b,1])
for snc in range(0,b):
    if snc==0:
        Y[snc]=y0+dY[snc]
        X[snc]=x0+dX[snc]
    else:
        Y[snc]=Y[snc-1]+dY[snc]
        X[snc]=X[snc-1]+dX[snc]    
            
sonuc=np.array([Y,X])
sonuc=np.transpose(sonuc)
print(sonuc)        
