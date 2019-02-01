import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as C
from datetime import datetime
import pandas as pd
import time

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

Rn = int(input('常温结电阻（以欧姆为单位）：'))
Cq = int(input('qubit的电容值（以fF为单位：）'))

#对于铝结，温度为30mk
T = 20e-3 #单位开尔文
delta = 200*C.e*1e-6 #单位焦

Rq = C.h/C.e**2
Ec = C.e**2/2/(Cq*1e-15)
Ic = C.pi*delta/2/C.e/Rn*np.tanh(delta/2/C.k/T)
Ej = Ic*C.h/4/C.e/C.pi

#Ej/C.h = Rq/Rj*delta/8/C.h
f01 = np.sqrt(8*Ej*Ec/C.h**2)-Ec/C.h

para = {'日期：':now, '结电阻Rn(欧姆）':Rn, '十字叉对地电容Cq(fF)':Cq, '温度T（开尔文）':T, '铝结能隙delta（焦）':delta, 'Ic(nA)': Ic*1e9, 'Ej(GHz)':Ej/C.h*1e-9, 'f01(GHz)':f01*1e-9}

pd.DataFrame(para,index=[1])

with open(datetime.now().date().isoformat()+'.txt', 'wb') as f: 
    f.write(str(para).encode('utf-8'))