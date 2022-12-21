
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import seaborn as sn
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt 
import math
X = []
y = []
trainMse = []
exp = [[2.27355,8.053799805],[1.6914,8.34521875],[1.37666,8.690143555], [1.27861,9.254519531],[2.01798,3.11382251]]
for i in range(0,5):
    x = pd.read_csv('/notebooks/compeng project/fractureG' + str(i) + '.csv').to_numpy()
    dam = pd.read_csv('/notebooks/compeng project/damage_parametersG' + str(i) + '.csv').to_numpy()
    for j in range(0, len(x)):
        if(x[j].sum() != 0 and mean_squared_error(x[j][0:2],exp[i]) <= 3):
            X.append(x[j])
            y.append(dam[j])
            # trainMse.append()


for j in range(0, len(X)):
    for i in range(0,2):
        X[j][i] = (X[j][i] - min(np.array(X)[:,i]))/(max(np.array(X)[:,i]) - min(np.array(X)[:,i]))
    # x.drop(columns = ["Displacement","Force","S_Max","S_Min","S_Mid","PEEQ","TRIAX","Load Angle"])
    # x.columns =['Disp','Force','Smax','Smin','Smid','PEEQ',"TRIAX","Angle"]
print(len(X))

X_train, X_test, y_train, y_test = train_test_split( np.array(X)[:, :2], np.array(y), test_size=0.33)
X_test = pd.DataFrame(X_test, columns = ['Displacement','Force'])
print(X_test)

print(np.append(X, y, axis=1))
corrMatrix = pd.DataFrame(np.append(X, y, axis=1),columns = ["Displacement","Force","S_Max","S_Min","S_Mid","PEEQ","TRIAX","Load Angle", "d1", "d2", "d3", "d4"]).corr()
plt.subplots(figsize=(10,10)) 
sn.heatmap(corrMatrix, annot=True)
plt.show()

from sklearn.neural_network import MLPRegressor


num_layers = [1,2,3,4,6,8,10,20]    # number of hidden layers
num_neurons = 30

mlp_tr_errors = []          
mlp_val_errors = []

for i, num in enumerate(num_layers):
    hiden_layer_sizes = tuple([num_neurons]*num)
    #Sklearn MLPRegressor default score 
    regr = MLPRegressor(random_state=1, max_iter=1000, hidden_layer_sizes = hiden_layer_sizes, solver='sgd', learning_rate='adaptive', shuffle= False).fit(X_train, y_train)
    print("Layers: " + str(num_layers[i]) + " Nodes" + str(hiden_layer_sizes[0]))
    print("G0: " + str(regr.predict([[2.27355,8.053799805]]))) #G0 fracture point
    print("G1: " + str(regr.predict([[1.6914,8.34521875]]))) #G1 fracture point
    print("G2: " + str(regr.predict([[1.37666,8.690143555]]))) #G2 fracture point
    print("G3: " + str(regr.predict([[1.27861,9.254519531]]))) #G3 
    print("G4: " + str(regr.predict([[2.01798,3.11382251]]))) #G4
    print("R: " + str(regr.predict([[0.5,3]]))) #R 

    #print("Score: " + str(regr.score(X_test, y_test)))
    tr_error = mean_squared_error(y_train, (regr.predict(X_train)))
    test_error = mean_squared_error(y_test, (regr.predict(X_test)))
    print("Train MSE: " + str(tr_error) + " Test MSE: " + str(test_error))
    
    mlp_tr_errors.append(tr_error)
    mlp_val_errors.append(test_error)
