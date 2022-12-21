from ast import Lambda
from asyncore import write
from operator import delitem
from sys import float_info
from turtle import color, st
import pandas as pd
import numpy as np
from pkg_resources import yield_lines
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math
import csv
from sklearn import preprocessing

eur = 2.71828

data = np.genfromtxt('TD\TD.csv', delimiter=',')
data_strain = data[:,0]
data_stress = data[:,1]

# take only max stress value
maxV = data_stress.argmax()
data_strain = data_strain[:maxV]
data_stress = data_stress[:maxV]
X = data_strain.astype(np.float64)
Y = data_stress.astype(np.float64)

def swiftVoce(x , a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2):
    return np.piecewise(x, [x<100],[lambda x:a1*(b1*(c1+x)**d1)+(1-a1)*(e1+(f1-e1)*eur**(-g1*x)), lambda x:a2*(b2*(c2+x)**d2)+(1-a2)*(e2+(f2-e2)*eur**(-g2*x))])


def swiftVoceT(x, a, b, c, d, e, f, g):
    return a*(b*(c+x)**d)+(1-a)*(e+(f-e)*eur**(-g*x))

    

popt, pcov= curve_fit(swiftVoce, X[286:], Y[286:], maxfev= 100000000 , bounds=((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (1, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, 1, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf)))
popt1, pcov1= curve_fit(swiftVoceT, X, Y, maxfev= 100000000, bounds=((0, 0, 0, 0, 0, 0, 0), (1, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf)))


# popt1 contains parameters for not piecewise function
a, b, c, d, e, f, g = popt1
print(a,b,c,d,e,f,g)



a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2  = popt
print(a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2) 

fig1, ax1 = plt.subplots()


x_line = np.arange(0,3.01,0.01)
y_line = swiftVoce(x_line, a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2)


plt.figure(1)
plt.scatter(X,Y)
plt.plot(x_line, y_line, color = 'red')
print(y_line[y_line.size-1])
plt.show()
