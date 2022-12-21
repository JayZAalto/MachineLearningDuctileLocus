import numpy as np
from sklearn.neural_network import MLPRegressor
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, accuracy_score, mean_absolute_error
from sklearn.datasets import load_iris
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel
from sklearn import preprocessing
from sklearn import preprocessing as pre
from matplotlib import pyplot as plt 

# When only using Force and displacement

X = pd.read_csv("fractures.csv").to_numpy()[:,:1]
y = pd.read_csv("finalGP.csv").to_numpy()
""" X = preprocessing.normalize(X)
y = preprocessing.normalize(y) """
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=21)

## For MLP Regressor
mlpr = MLPRegressor(hidden_layer_sizes= tuple([3]*2), activation = 'relu', random_state=21, solver='lbfgs')
mlpr.fit(X_train, y_train)

y_pred_val = mlpr.predict(X_val)

print("Mean percentage error for MLP regression : ",mean_squared_error(y_val, y_pred_val))



print("Converged Damage paramters when only using Force and Displacement: ", mlpr.predict(np.asarray([2.01798]).reshape(1,-1)))
print("Converged Damage paramters when only using Force and Displacement: ", mlpr.predict(np.asarray([1.27861]).reshape(1,-1)))
print("Converged Damage paramters when only using Force and Displacement: ", mlpr.predict(np.asarray([1]).reshape(1,-1)))


num_layers = [1,2,3,4,6,7,8,9,10,20,30 ,40]    # number of hidden layers
num_neurons = 3

mlp_tr_errors = []          
mlp_val_errors = []

for i, num in enumerate(num_layers):
    hiden_layer_sizes = tuple([num_neurons]*num)
    #Sklearn MLPRegressor default score 
    regr = MLPRegressor(random_state=1, max_iter=1000, hidden_layer_sizes = hiden_layer_sizes, solver='sgd', learning_rate='adaptive', shuffle= False).fit(X_train, y_train)

    #print("Score: " + str(regr.score(X_test, y_test)))
    tr_error = mean_squared_error(y_train, (regr.predict(X_train)))
    test_error = mean_squared_error(y_val, (regr.predict(X_val)))
    print("Train MSE: " + str(tr_error) + " Test MSE: " + str(test_error))
    
    mlp_tr_errors.append(tr_error)
    mlp_val_errors.append(test_error)


plt.figure(figsize=(8, 6))

plt.plot(num_layers, mlp_tr_errors, label = 'Train')
plt.plot(num_layers, mlp_val_errors,label = 'Test')
plt.xticks(num_layers)
plt.legend(loc = 'upper left')

plt.xlabel('Layers')
plt.ylabel('Loss')
plt.title('Train vs test loss')
plt.show()
