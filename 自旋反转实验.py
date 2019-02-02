#本实验目的是考察微观可逆性到宏观不可逆性
import numpy as np
import matplotlib.pyplot as plt
import random
print ("请输入粒子总数n")
n=int(input())
print("请输入反转概率")
v=float(input())
print("请输入演化时间t")
t1=int(input())
time=[]
time.append(0)
result=[]
result.append(1)
s=[1]*n #初始化所有粒子的自旋为1
for j in range(0,t1):   #该循环嵌套用来确定j时刻每个粒子的自旋状态
    for i in range(0,n):
        x=random.random()
        if x<=v:
            s[i]=-s[i]
        else:
            s[i]=s[i]
    m=np.sum(s) #计算j时刻该自旋环的总磁矩
    time.append(j+1) #将时间序列依次写入列表
    result.append(m/n) #将每时刻的平均磁矩依次写入列表
plt.plot(time,result,'-')
plt.show()
import xlwt
moni=xlwt.Workbook()
sheet1=moni.add_sheet('zsk') #创建sheet
for q in range(0,t1):
    sheet1.write(q,0,time[q]) #将time写入第一列
    sheet1.write(q,1,result[q]) #将result写入第二列
    moni.save('data.xls')  #将数据保存为excel文件

