import pandas as pd
import matplotlib.pyplot as plt
import csv
import sys

# G4_P_LS_Cr2.rpt
filenamels = sys.argv[1]


# G4_P_FD.rpt
filenamefd = sys.argv[2]

# P${number}
pname = sys.argv[3]

ls_sdv = pd.read_fwf(filenamels)[2:]



sdv16 = ls_sdv['Unnamed: 5'].astype(float)

sMax = ls_sdv['S:Max Principal P'].astype(float)
sMid = ls_sdv['S:Mid Principal P'].astype(float)
sMin = ls_sdv['S:Min Principal P'].astype(float)

peeq = ls_sdv['Unnamed: 4'].astype(float)
triax = ls_sdv['Unnamed: 10'].astype(float)
loadAngle = ls_sdv['Unnamed: 11'].astype(float)


i = 2
index = -1
for j in sdv16:
    if(j>=0.9):
        index = i
        if (j==1):	   
            break;
    i+=1
frame = ls_sdv['Unnamed: 0'].astype(float)



df_FEM = pd.read_fwf(filenamefd)
df_Experi = pd.read_csv("G4_Expri.csv")
fdFrame = df_FEM['X']



X = df_FEM["Disp"]
y = df_FEM["Force"]


X_Experi = df_Experi["Disp"]
y_Experi = df_Experi["Force"]

if index != -1:
    i = 0
    num=0
    for x in fdFrame:
        if(x == frame[index]):
            num = i
            break;
        i+=1
    with open('fracture.csv', 'a') as f:
        writer = csv.writer(f)
        ps1 =[X[num], y[num], sMax[index], sMid[index], sMin[index], peeq[index], triax[index], loadAngle[index]]
        writer.writerow(ps1)

    plt.plot(X_Experi, y_Experi, '--o', color = 'black', markevery=30)
    plt.plot(X_Experi[0], y_Experi[0], '--o', color = 'black', label = '_nolegend_')
    plt.plot(X_Experi[X_Experi.size-1], y_Experi[y_Experi.size-1], '--o', color = 'black', label = '_nolegend_')
    plt.plot(X[:num+1], y[:num+1], color = 'blue')
    plt.plot(X[num],y[num], '*', color = 'red', markersize=15)
    plt.legend(['Experimental', 'FEM', 'Fracture point'], loc = 4)
    plt.xlabel("Displacement mm")
    plt.ylabel("Force N")
    plt.ylim([0,3.5])
    plt.xlim([0,2.3]) 
    plt.title("G4 FEM ML model 4 vs Experimental") 
    plt.savefig("G4 FEM ML model 4 vs Experimental")

else:
    plt.plot(X_Experi, y_Experi, '--o', color = 'black', markevery=30)
    plt.plot(X_Experi[0], y_Experi[0], '--o', color = 'black', label = '_nolegend_')
    plt.plot(X_Experi[X_Experi.size-1], y_Experi[y_Experi.size-1], '--o', color = 'black', label = '_nolegend_')
    plt.plot(X, y, color = 'blue')
    plt.legend(['Experimental', 'FEM', 'Fracture point'], loc = 4)
    plt.xlabel("Displacement mm")
    plt.ylabel("Force N")
    plt.title("G4 FEM ML model 4 vs Experimental") 
    plt.savefig("G4 FEM ML model 4 vs Experimental")
