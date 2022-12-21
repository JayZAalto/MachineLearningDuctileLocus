import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import csv
import os
import glob
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, accuracy_score, mean_absolute_error, r2_score
from sklearn.datasets import load_iris
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from sklearn import preprocessing
from sklearn import preprocessing as pre

arr = np.empty([1,905])
columns = ["Displacement frac.", "Force frac."]

for i in range(0,301):
    columns.append("PEEQ frame" + str(i))
for i in range(0,301):
    columns.append("Triaxility frame" + str(i))
for i in range(0,301):
    columns.append("Load Angle frame" + str(i))

# For G0

fd0 = genfromtxt(r"G0\fractureFD_G0.csv", delimiter=',')
count=0
for i in 1,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24:
    peeq = pd.read_csv(r"G0\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 9'], axis=1).to_numpy()
    triax = pd.read_csv(r"G0\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 9'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"G0\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 4'], axis=1).to_numpy()
    pad = [0]*(903-(len(peeq)*3))
    a = np.array(pad).reshape(-1,1).reshape(1,-1)
    b=fd0[count].reshape(2,1).tolist()
    newarr = np.array((b+peeq.tolist()+triax.tolist()+load_angle.tolist())).reshape(1,-1)
    newarr = np.append(newarr,a).reshape(-1,1).reshape(1,-1)
    if i == 1:
        arr = newarr
    else:
        arr=np.append(arr,newarr)
    count+=1

arr = np.expand_dims(arr, axis=(0, 1)).reshape(count,905).astype(float)
arr[np.isnan(arr)] = 0



# For G1
index =0
fd1 = genfromtxt(r"G1\fractureFD_G1.csv", delimiter=',')
for i in 1,3,4,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,23,24:
    peeq = pd.read_csv(r"G1\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 10','Unnamed: 11'], axis=1).to_numpy()
    triax = pd.read_csv(r"G1\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 11'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"G1\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 10'], axis=1).to_numpy()
    pad = [0]*(903-(len(peeq)*3))
    a = np.array(pad).reshape(-1,1).reshape(1,-1)
    b=fd1[index].reshape(2,1).tolist()
    newarr = np.array((b+peeq.tolist()+triax.tolist()+load_angle.tolist()), dtype=object).reshape(1,-1)
    newarr = np.append(newarr,a)
    arr=np.append(arr,newarr)
    count+=1
    index+=1

arr = np.expand_dims(arr, axis=(0, 1)).reshape(count,905).astype(float)
#arr[np.isnan(arr)] = 0

# For G2
index =0
fd2 = genfromtxt(r"G2\fractureFD_G2.csv", delimiter=',')
for i in 1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24:
    peeq = pd.read_csv(r"G2\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 9','Unnamed: 10'], axis=1).to_numpy()
    triax = pd.read_csv(r"G2\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 1','Unnamed: 10'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"G2\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 1','Unnamed: 9'], axis=1).to_numpy()
    pad = [0]*(903-(len(peeq)*3))
    a = np.array(pad).reshape(-1,1).reshape(1,-1)
    b=fd2[index].reshape(2,1).tolist()
    newarr = np.array((b+peeq.tolist()+triax.tolist()+load_angle.tolist()), dtype=object).reshape(1,-1)
    newarr = np.append(newarr,a)
    arr=np.append(arr,newarr)
    count+=1
    index+=1

arr = np.expand_dims(arr, axis=(0, 1)).reshape(count,905).astype(float)
#arr[np.isnan(arr)] = 0

# For G3

index =0
fd3 = genfromtxt(r"G3\fractureFD_G3.csv", delimiter=',')
for i in 1,2,3,4,7,8,9,12,13,14,15,16,18,19,20,21,22,24:
    peeq = pd.read_csv(r"G3\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 9'], axis=1).to_numpy()
    triax = pd.read_csv(r"G3\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 9'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"G3\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 8'], axis=1).to_numpy()
    pad = [0]*(903-(len(peeq)*3))
    a = np.array(pad).reshape(-1,1).reshape(1,-1)
    b=fd3[index].reshape(2,1).tolist()
    newarr = np.array((b+peeq.tolist()+triax.tolist()+load_angle.tolist()), dtype=object).reshape(1,-1)
    newarr = np.append(newarr,a)
    arr=np.append(arr,newarr)
    count+=1
    index+=1

arr = np.expand_dims(arr, axis=(0, 1)).reshape(count,905).astype(float)
#arr[np.isnan(arr)] = 0


# For G4
index =0
fd4 = genfromtxt(r"G4\fractureFD_G4.csv", delimiter=',')
for i in 11,13,22,23,24:
    peeq = pd.read_csv(r"G4\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 9','Unnamed: 11','Unnamed: 12'], axis=1).to_numpy()
    triax = pd.read_csv(r"G4\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 12'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"G4\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4', 'Unnamed: 8','Unnamed: 9','Unnamed: 11'], axis=1).to_numpy()
    pad = [0]*(903-(len(peeq)*3))
    a = np.array(pad).reshape(-1,1).reshape(1,-1)
    b=fd4[index].reshape(2,1).tolist()
    newarr = np.array((b+peeq.tolist()+triax.tolist()+load_angle.tolist()), dtype=object).reshape(1,-1)
    newarr = np.append(newarr,a)
    arr=np.append(arr,newarr)
    count+=1
    index+=1
arr = np.expand_dims(arr, axis=(0, 1)).reshape(count,905).astype(float)
arr[np.isnan(arr)] = 0
X=pd.DataFrame(arr,columns = columns)
X=X[np.isfinite(X).all(1)]
print(X[np.isfinite(X).all(1)].shape)
print(np.array(X)[1,0])

for i in range(0,905):
    mini = min(np.array(X)[:,i])
    maxi = max(np.array(X)[:,i])
    print(str(i) )
    for j in range(0, len(X)):
        X[j,i] = (np.array(X)[j,i] - mini)/(maxi - mini)

y = pd.read_csv("finalGP.csv").to_numpy()


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=21)
print(X_val)
mlpr = MLPRegressor(hidden_layer_sizes= (1,14), activation = 'relu', random_state=21, solver='lbfgs', max_iter=100000)
mlpr.fit(X_train, y_train)

import shap
shap.initjs()
#regr = MLPRegressor(random_state=1, max_iter=1000, hidden_layer_sizes =  tuple([30]*6), solver='sgd', learning_rate='adaptive', shuffle= False).fit(X_train, y_train)
sh = shap.KernelExplainer(mlpr.predict, X_train)
shap_values = sh.shap_values(X_val)
shap.summary_plot(shap_values[3],X_val, max_display=20)
