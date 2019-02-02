import numpy as np
import math
import random 
import matplotlib.pyplot as plt
N=64
L=10
vmax=0.1
r=[[0 for i in range(N)] for i in range(3)]
v=[[0 for i in range(N)] for i in range(3)]
a=[[0 for i in range(N)] for i in range(3)]
def initialize():
    n=int(math.ceil(math.pow(N,1.0/3)))
    a=L/n
    p=0
    for x in range(0,n):
        for y in range(0,n):
            for z in range(0,n):
                if(p<N):
                    r[0][p]=(x+0.5)*a
                    r[1][p]=(y+0.5)*a
                    r[2][p]=(z+0.5)*a
                p+=1
    for p in range(0,N):
        for i in range(0,3):
            v[i][p]=vmax*(random.random())
def computeacceleration():
    for i in range(0,N):
        for k in range(0,3):
            a[k][i]=0
    for i in range(0,N-1):
        for j in range(i+1,N):
            rij=[0 for i in range(3)]
            rsqd=0
            for k in range(0,3):
                rij[k]=r[k][i]-r[k][j]
                rsqd+=rij[k]**2
            f=24*(2*math.pow(rsqd,-7)-math.pow(rsqd,-4))
            for k in range(0,3):
                a[k][i]+=rij[k]*f
                a[k][j]-=rij[k]*f
def velocityverlet(dt):
    computeacceleration()
    for i in range(0,N):
        for k in range(0,3):
            r[k][i]+=v[k][i]*dt+0.5*a[k][i]*dt**2
            v[k][i]+=0.5*a[k][i]*dt
    computeacceleration()
    for i in range(0,N):
        for k in range(0,3):
            v[k][i]+=0.5*a[k][i]*dt
def instantaneoustemperature():
    sums=0
    for i in range(0,N):
        for k in range(0,3):
            sums+=v[k][i]**2
    return sums/(3*(N-1))
initialize()
dt=0.1
t=[0 for i in range(3000)]
result=[0 for i in range(3000)]
#f=open('T.data','w')
for i in range(0,3000):
    velocityverlet(dt)
    t[i]=i*dt
    result[i]=instantaneoustemperature()
    #f.write(str(instantaneoustemperature()))
#f.close()
'''import xlwt
moni=xlwt.Workbook()
sheet1=moni.add_sheet('zsk') #创建sheet
for q in range(0,3000):
    sheet1.write(q,0,t[q]) #将time写入第一列
    sheet1.write(q,1,result[q]) #将result写入第二列
    moni.save('data.xls')  #将数据保存为excel文件
print('end')
'''
plt.plot(t,result,'-r')
plt.show()
