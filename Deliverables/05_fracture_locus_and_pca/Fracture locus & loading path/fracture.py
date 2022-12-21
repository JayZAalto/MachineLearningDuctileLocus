import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import sys

localFiles = []
globalFiles = []
name = "model_2_data"

for i in range(0,5):
    localFiles.append(name + "/G" + str(i) + "_P_LS_Cr2.rpt")
    globalFiles.append(name + "/G" + str(i) + "_P_FD.rpt")
    
for i in range(0,5):
    print(str(i) + ": ")
    print(pd.read_fwf(localFiles[i]).head(1))
    print(pd.read_fwf(globalFiles[i]).head(1))
    print("\n")

uncleanLocalData = []
localData = []
globalData = []

for i in range(0,5):
    data = pd.read_fwf(globalFiles[i])
    globalData.append([data["Disp"], data["Force"]])
    uncleanLocalData.append(pd.read_fwf(localFiles[i])[2:])
#SDV16 fracture SDV20 triax SDV22 load angle
localData.append([uncleanLocalData[0]['Unnamed: 5'].astype(float), uncleanLocalData[0]['Unnamed: 8'].astype(float), uncleanLocalData[0]['Unnamed: 9'].astype(float), uncleanLocalData[0]['Unnamed: 4'].astype(float)]) #G0
localData.append([uncleanLocalData[1]['Unnamed: 5'].astype(float), uncleanLocalData[1]['Unnamed: 10'].astype(float), uncleanLocalData[1]['Unnamed: 11'].astype(float), uncleanLocalData[1]['Unnamed: 4'].astype(float)]) #G1
localData.append([uncleanLocalData[2]['Unnamed: 6'].astype(float), uncleanLocalData[2]['Unnamed: 9'].astype(float), uncleanLocalData[2]['Unnamed: 10'].astype(float), uncleanLocalData[2]['Unnamed: 1'].astype(float)]) #G2
localData.append([uncleanLocalData[3]['Unnamed: 5'].astype(float), uncleanLocalData[3]['Unnamed: 8'].astype(float), uncleanLocalData[3]['Unnamed: 9'].astype(float),uncleanLocalData[3]['Unnamed: 4'].astype(float)]) #G3
localData.append([uncleanLocalData[4]['Unnamed: 5'].astype(float), uncleanLocalData[4]['Unnamed: 10'].astype(float), uncleanLocalData[4]['Unnamed: 11'].astype(float),uncleanLocalData[4]['Unnamed: 4'].astype(float)]) #G4


fractPoint = []
startPoint = []
for i in range(0,4):
    fractPoint.append(max(j for j in range(2,len(localData[i][0])+2) if localData[i][0][j] >= 0.89 and localData[i][0][j] <= 1)- 1)
    startPoint.append(min(j for j in range(2,len(localData[i][0])+2) if localData[i][0][j] > 0)- 1)

    
color1 = ['r:', 'b:', 'm:', 'k:']
color2 = ['or', 'ob', 'om', 'ok']


for i in range(0,4):
    plt.plot(localData[i][1][startPoint[i]:fractPoint[i]], localData[i][3][startPoint[i]:fractPoint[i]], color1[i])
for i in range(0,4):
    plt.plot(localData[i][1][fractPoint[i]+1], localData[i][3][fractPoint[i]+1], color2[i])


plt.legend(['G0', 'G1', 'G2', 'G3'])
plt.ylabel("Damage strain")
plt.xlabel("Stress triaxility")
plt.gca().set_xlim([0, 1])
# plt.title("G4 Damage simulation  vs Experimental") 
plt.savefig(str(name) + "1")
plt.clf()

for i in range(0,4):
    plt.plot(localData[i][2][startPoint[i]:fractPoint[i]], localData[i][3][startPoint[i]:fractPoint[i]], color1[i])
for i in range(0,4):
    plt.plot(localData[i][2][fractPoint[i]+1], localData[i][3][fractPoint[i]+1], color2[i])

plt.legend(['G0', 'G1', 'G2', 'G3'])
plt.ylabel("Damage strain")
plt.xlabel("Lode angle parameter")
plt.gca().set_xlim([0, 1])
# plt.title("G4 Damage simulation  vs Experimental") 
plt.savefig(str(name) + "2")
plt.clf()



fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
from matplotlib import cm
ax.set_xlabel('Lode angle parameter')
ax.set_ylabel('Stress triaxility')
ax.set_zlabel('Damage strain')
X = []
Y = []
Z = []
for i in range(0,4):
    X.append(localData[i][2][fractPoint[i]+1])
    Y.append(localData[i][1][fractPoint[i]+1])
    Z.append(localData[i][3][fractPoint[i]+1])


import math

x_test = np.linspace(-1, 1, 1000)
y_test = np.linspace(-0.33, 1, 1000)

z_test= []
from scipy.optimize import least_squares
def fun(p, x, y, z):
    return [(p[0] * math.exp((-p[1])*y[0]) - p[2] * math.exp((-p[3])*y[0]))*((x[0])**2) + p[2] * math.exp((-p[3])*y[0]) - z[0],
            (p[0] * math.exp((-p[1])*y[1]) - p[2] * math.exp((-p[3])*y[1]))*((x[1])**2) + p[2] * math.exp((-p[3])*y[1]) - z[1],
            (p[0] * math.exp((-p[1])*y[2]) - p[2] * math.exp((-p[3])*y[2]))*((x[2])**2) + p[2] * math.exp((-p[3])*y[2]) - z[2],
            (p[0] * math.exp((-p[1])*y[3]) - p[2] * math.exp((-p[3])*y[3]))*((x[3])**2) + p[2] * math.exp((-p[3])*y[3]) - z[3]]
#1.45, 1.47, 1.26, 1.52 erald
#1.46, 1.48, 1.31, 1.36 shreyas
p0 = [1.45, 1.47, 1.26, 1.52]
res_lsq = least_squares(fun, p0, args=(X,Y,Z),bounds=([0.01,0.01,0.01,0.01],[3,3,3,3]), method='dogbox', xtol=1e-14, ftol=1e-14, gtol=1e-14)



def fun_fixX(p, x, y): 
    res = []
    for i in range(0, len(y)):
        res.append((p[0] * math.exp((-p[1])*y[i]) - p[2] * math.exp((-p[3])*y[i]))*((x)**2) + p[2] * math.exp((-p[3])*y[i]))
    return res
def fun_fixY(p, x, y): 
    res = []
    for i in range(0, len(x)):
        res.append((p[0] * math.exp((-p[1])*y) - p[2] * math.exp((-p[3])*y))*((x[i])**2) + p[2] * math.exp((-p[3])*y))
    return res

def fun_fixZ(p, y, z): 
    res = []
    for i in range(0, len(y)):
        notneg = (z - p[2] * math.exp((-p[3])*y[i]))/(p[0] * math.exp((-p[1])*y[i]) - p[2] * math.exp((-p[3])*y[i]))
        if notneg >= 0:
            res.append( math.sqrt(notneg)) 
        else:
            res.append(np.nan)
    return res


#pf = res_lsq.x
pf = p0
print(res_lsq.x)
for i in range(0, 1000):
    tmp = []
    for j in range(0, 1000):
       
        
        calc = (pf[0] * math.exp((-pf[1])*y_test[i]) - pf[2] * math.exp((-pf[3])*y_test[i]))*((x_test[j])**2) + pf[2] * math.exp(-pf[3]*y_test[i])
        if calc <= 3.5 and calc >= 0:
            tmp.append(calc)
        else:
            tmp.append(np.nan)
    z_test.append(tmp)
x_test, y_test = np.meshgrid(x_test, y_test)

ax.set_zlim(0, 3.5)
ax.set_xlim(-1, 1)
ax.set_ylim(-0.33, 1)
surf = ax.plot_surface(x_test, y_test,np.array(z_test),cmap=cm.coolwarm, linewidth=1, antialiased=False)

color1 = ['y', 'g', 'm', 'k']
color2 = ['oy', 'og', 'om', 'ok']
for i in range(0,4):
    plt.plot(localData[i][2][startPoint[i]:fractPoint[i]],localData[i][1][startPoint[i]:fractPoint[i]], localData[i][3][startPoint[i]:fractPoint[i]], color1[i])
for i in range(0,4):
    ax.plot(localData[i][2][fractPoint[i]+1],localData[i][1][fractPoint[i]+1], localData[i][3][fractPoint[i]+1], color2[i], zorder=5, label="G" + str(i))
fig.colorbar(surf, shrink=0.5, aspect=5, location = 'left')
ax.set_title(pf)
ax.legend()

angle = 55
ax.view_init(angle/(2.7), angle)
plt.draw()
plt.pause(5)

color1 = ['r', 'b', 'm', 'k']
color2 = ['or', 'ob', 'om', 'ok']
plt.rcParams['figure.figsize'] = [10, 16]



fig, axs = plt.subplots(3, 2)

ax = axs[0, 0]
for i in range(0,4):
    ax.set_ylim([0, 0.9])
    ax.set_xlim([0, 1])
    ax.plot(np.linspace(-0.5, 1.5, 1000), fun_fixX(p0,localData[i][2][fractPoint[i]+1],np.linspace(-0.5, 1.5, 1000) ), color1[i], label="G" + str(i))
    ax.plot(localData[i][1][fractPoint[i]+1], localData[i][3][fractPoint[i]+1], color2[i])
ax.set_title("model 2" ) 
ax.set_ylabel("Damage strain")
ax.set_xlabel("Stress triaxility") 
ax.legend()
ax = axs[1, 0]
for i in range(0,4):    
    ax.set_ylim([0, 0.9])
    ax.set_xlim([0, 1])
    ax.plot(np.linspace(-0.5, 1.5, 1000), fun_fixY(p0,np.linspace(-0.5, 1.5, 1000),localData[i][1][fractPoint[i]+1]), color1[i], label="G" + str(i))
    ax.plot(localData[i][2][fractPoint[i]+1], localData[i][3][fractPoint[i]+1], color2[i])
    
ax.set_title("model 2" ) 
ax.set_ylabel("Damage strain")
ax.set_xlabel("Lode angle parameter")
ax.legend()


ax = axs[2, 0]

for i in range(0,4):
    ax.set_ylim([0, 0.9])
    ax.set_xlim([0, 1])
    ax.plot(np.linspace(0, 1.5, 1000), fun_fixZ(p0,np.linspace(0, 1, 1000),localData[i][3][fractPoint[i]+1]), color1[i], label="G" + str(i))
    ax.plot(localData[i][1][fractPoint[i]+1], localData[i][2][fractPoint[i]+1], color2[i])
    

ax.set_title("model 2") 
ax.set_ylabel("Stress triaxility")
ax.set_xlabel("Lode angle parameter")
ax.legend()
  
    
    
    
    

ax = axs[0, 1]

for i in range(0,4):
    ax.set_ylim([0, 0.9])
    ax.set_xlim([0, 1])
    ax.plot(np.linspace(-0.5, 1.5, 1000), fun_fixX(pf,localData[i][2][fractPoint[i]+1],np.linspace(-0.5, 1.5, 1000) ), color1[i], label="G" + str(i))
    ax.plot(localData[i][1][fractPoint[i]+1], localData[i][3][fractPoint[i]+1], color2[i])
    

ax.set_title("best fit (least squares)") 
ax.set_ylabel("Damage strain")
ax.set_xlabel("Stress triaxility")
ax.legend()
  
ax = axs[1, 1]

for i in range(0,4):
    ax.set_ylim([0, 0.9])
    ax.set_xlim([0, 1])
    ax.plot(np.linspace(-0.5, 1.5, 1000), fun_fixY(pf,np.linspace(-0.5, 1.5, 1000),localData[i][1][fractPoint[i]+1]), color1[i], label="G" + str(i))
    ax.plot(localData[i][2][fractPoint[i]+1], localData[i][3][fractPoint[i]+1], color2[i])
    
ax.set_title("best fit (least squares)") 
ax.set_ylabel("Damage strain")
ax.set_xlabel("Lode angle parameter")
ax.legend()

ax = axs[2, 1]

for i in range(0,4):
    ax.set_ylim([0, 0.9])
    ax.set_xlim([0, 1])
    ax.plot(np.linspace(0, 1.5, 1000), fun_fixZ(pf,np.linspace(0, 1, 1000),localData[i][3][fractPoint[i]+1]), color1[i], label="G" + str(i))
    ax.plot(localData[i][1][fractPoint[i]+1], localData[i][2][fractPoint[i]+1], color2[i])
    

ax.set_title("best fit (least squares)") 
ax.set_ylabel("Stress triaxility")
ax.set_xlabel("Lode angle parameter")
ax.legend()
  

plt.show()

