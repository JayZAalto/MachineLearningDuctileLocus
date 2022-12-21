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

# For G0

fd0 = genfromtxt(r"C:\Users\giris\Documents\Project\ML_test\new_test\G0\fractureFD_G0.csv", delimiter=',')
count=0
for i in 1,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24:
    peeq = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G0\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 9'], axis=1).to_numpy()
    triax = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G0\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 9'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G0\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 4'], axis=1).to_numpy()
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
fd1 = genfromtxt(r"C:\Users\giris\Documents\Project\ML_test\new_test\G1\fractureFD_G1.csv", delimiter=',')
for i in 1,3,4,5,6,7,9,10,11,12,13,14,16,17,18,19,20,21,23,24:
    peeq = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G1\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 10','Unnamed: 11'], axis=1).to_numpy()
    triax = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G1\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 11'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G1\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 10'], axis=1).to_numpy()
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
fd2 = genfromtxt(r"C:\Users\giris\Documents\Project\ML_test\new_test\G2\fractureFD_G2.csv", delimiter=',')
for i in 1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24:
    peeq = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G2\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 9','Unnamed: 10'], axis=1).to_numpy()
    triax = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G2\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 1','Unnamed: 10'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G2\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 1','Unnamed: 9'], axis=1).to_numpy()
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
fd3 = genfromtxt(r"C:\Users\giris\Documents\Project\ML_test\new_test\G3\fractureFD_G3.csv", delimiter=',')
for i in 1,2,3,4,7,8,9,12,13,14,15,16,18,19,20,21,22,24:
    peeq = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G3\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 9'], axis=1).to_numpy()
    triax = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G3\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 9'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G3\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 8'], axis=1).to_numpy()
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
fd4 = genfromtxt(r"C:\Users\giris\Documents\Project\ML_test\new_test\G4\fractureFD_G4.csv", delimiter=',')
for i in 11,13,22,23,24:
    peeq = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G4\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 8','Unnamed: 9','Unnamed: 11','Unnamed: 12'], axis=1).to_numpy()
    triax = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G4\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4','Unnamed: 8','Unnamed: 9','Unnamed: 12'], axis=1).to_numpy()
    load_angle = pd.read_csv(r"C:\Users\giris\Documents\Project\ML_test\new_test\G4\fractureLS_P"+str(i)+r".csv").drop(['Unnamed: 0','S:Max Principal P','S:Mid Principal P','S:Min Principal P','Unnamed: 4', 'Unnamed: 8','Unnamed: 9','Unnamed: 11'], axis=1).to_numpy()
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



y = pd.read_csv("finalGP.csv").to_numpy()

X_train, X_val, y_train, y_val = train_test_split(arr, y, test_size=0.3, random_state=21)

mlpr = MLPRegressor(hidden_layer_sizes= (1,14), activation = 'relu', random_state=21, solver='lbfgs', max_iter=100000)
mlpr.fit(X_train, y_train)

y_pred_val = mlpr.predict(X_val)

print("Mean percentage error for MLP regression : ",mean_squared_error(y_val, y_pred_val))
print(mlpr.score(X_val, y_val))
print(mlpr.predict(arr[86,:].reshape(1,-1)))