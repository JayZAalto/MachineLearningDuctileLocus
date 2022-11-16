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

eur = 2.71828
fileName = input('Enter the csv data file without ".csv": ')

data = np.genfromtxt(fileName+'.csv', delimiter=',')
data_strain = data[:,0]
r_val = data[:,1]

# take only max stress value
maxV = r_val.argmax()
data_strain = data_strain[:maxV]
data_stress = r_val[:maxV]
X = data_strain.astype(np.float64)
Y = data_stress.astype(np.float64)

def swiftVoce(x , C11, C12, C13, C21, C22, C23):
    return np.piecewise(x, [x<0],[lambda x:C11 + C12*(1-eur**(-C13*x)), lambda x:C21 + C22*(1-eur**(-C23*x))])


def swiftVoceT(x, C1, C2, C3):
    return C1 + C2*(1-eur**(-C3*x))

    

popt, pcov= curve_fit(swiftVoce, X[96:], Y[96:], maxfev= 100000000 , bounds=((0, 0, 0, 0, 0, 0), (np.inf, np.inf, np.inf, np.inf, np.inf, np.inf)))
popt1, pcov1= curve_fit(swiftVoceT, X, Y, maxfev= 100000000, bounds=((0, 0, 0), (np.inf, np.inf, np.inf)))


# popt1 contains parameters for not piecewise function
c1, c2, c3 = popt1
print(c1, c2, c3)



c11, c12, c13, c21, c22, c23 = popt
print(c11, c12, c13, c21, c22, c23)

fig1, ax1 = plt.subplots()

plt.figure(1)
plt.scatter(X,Y)
x_line_extend = np.arange(0, 3.01, 0.01)
x_line_extend_first = np.arange(0.008, 0.01, 0.00011764705)
x_line_extend_second = np.arange(0.01, 0.1, 0.001)
x_line_extend_third = np.arange(0.1, 3.01, 0.01)
y_line_extend_piecewise_first = swiftVoce(x_line_extend_first, c11, c12, c13, c21, c22, c23)
y_line_extend_piecewise_second = swiftVoce(x_line_extend_second, c11, c12, c13, c21, c22, c23)
y_line_extend_piecewise_third = swiftVoce(x_line_extend_third, c11, c12, c13, c21, c22, c23)
y_line_extend_single = swiftVoceT(x_line_extend, c1, c2, c3)
plt.plot(x_line_extend_first, y_line_extend_piecewise_first, color = 'red')
plt.plot(x_line_extend_second, y_line_extend_piecewise_second, color = 'red')
plt.plot(x_line_extend_third, y_line_extend_piecewise_third, color = 'red')
plt.plot(x_line_extend, y_line_extend_single, color = 'black')
plt.legend(['Uniaxial Tension FlowCurve',  'Piecewise function (small strain)', 'Piecewise function (large strain)','Single function'])
plt.xlabel("True Strain")
plt.ylabel("True Stress")
plt.title("Fitted Swift Voce curve extended to large strain")
plt.savefig('Fitted Swift Voce curve extended to large strain (R value DD)')
print(np.max(y_line_extend_piecewise_second))
print(np.max(y_line_extend_single))

plt.figure(2)
plt.scatter(X,Y)
x_line_maxStress = np.arange(0.0086, 0.166, 0.001)
y_line_maxStress_piecewise = swiftVoce(x_line_maxStress, c11, c12, c13, c21, c22, c23)
y_line_maxStress_single = swiftVoceT(x_line_maxStress, c1, c2, c3)
plt.plot(x_line_maxStress, y_line_maxStress_piecewise, color = 'red')
plt.plot(x_line_maxStress, y_line_maxStress_single, color = 'black')
plt.legend(['Uniaxial Tension FlowCurve',  'Piecewise function','Single function'])
plt.xlabel("True Strain")
plt.ylabel("True Stress")
plt.title("Fitted Swift Voce curve")
plt.savefig('Fitted Swift Voce curve (R value DD)')




plt.show()

with open('parameters_piecewise.csv', 'w') as f:
    writer = csv.writer(f)
    ps1 =[c11, c12, c13]
    ps2 =[c21, c22, c23]
    writer.writerow(ps1)
    writer.writerow(ps2)

with open('strain_piecewise.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for i in x_line_extend_first:
        writer.writerow([i])
    for i in x_line_extend_second:
        writer.writerow([i])
    for i in x_line_extend_third:
        writer.writerow([i])

with open('stress_piecewise.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for i in y_line_extend_piecewise_first:
        writer.writerow([i])
    for i in y_line_extend_piecewise_second:
        writer.writerow([i])
    for i in y_line_extend_piecewise_third:
        writer.writerow([i])
