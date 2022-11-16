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

plt.figure(1)
plt.scatter(X,Y)
x_line_extend_first = np.arange(0, 0.001, 0.0001)
x_line_extend_second = np.arange(0.001, 0.1, 0.001)
x_line_extend_third = np.arange(0.1, 3.01, 0.01)
x_line_extend_single = np.arange(0, 3.01, 0.01)
y_line_extend_piecewise_first = swiftVoce(x_line_extend_first, a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2)
y_line_extend_piecewise_second = swiftVoce(x_line_extend_second, a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2)
y_line_extend_piecewise_third = swiftVoce(x_line_extend_third, a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2)
y_line_extend_single = swiftVoceT(x_line_extend_single, a, b, c, d, e, f, g)
y_line_extend_single_first = swiftVoceT(x_line_extend_first, a, b, c, d, e, f, g)
y_line_extend_single_second = swiftVoceT(x_line_extend_second, a, b, c, d, e, f, g)

plt.plot(x_line_extend_first, y_line_extend_piecewise_first, color = 'red')
plt.plot(x_line_extend_second, y_line_extend_piecewise_second, color = 'red')
plt.plot(x_line_extend_third, y_line_extend_piecewise_third, color = 'red')
plt.plot(x_line_extend_single, y_line_extend_single, color = 'black')
plt.legend(['Uniaxial Tension FlowCurve',  'Piecewise function (small strain)', 'Piecewise function (large strain)','Single function'])
plt.xlabel("True Strain")
plt.ylabel("True Stress")
plt.title("Fitted Swift Voce curve extended to large strain")
print(np.max(y_line_extend_piecewise_third))
print(np.max(y_line_extend_single))
plt.savefig('Fitted Swift Voce curve extended to large strain (TD)')

plt.figure(2)
plt.scatter(X,Y)
x_line_maxStress = np.arange(0, 0.2, 0.001)
x_line_maxStress_peicewise_second = np.arange(0.022, 0.2, 0.001)
x_line_maxStress_peicewise_first = np.arange(0, 0.022, 0.001)

y_line_maxStress_piecewise = swiftVoce(x_line_maxStress_peicewise_second, a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2)
y_line_maxStress_single = swiftVoceT(x_line_maxStress, a, b, c, d, e, f, g)
y_line_maxStress_piecewise_first = swiftVoceT(x_line_maxStress_peicewise_first, a, b, c, d, e, f, g)

plt.plot(x_line_maxStress_peicewise_first, y_line_maxStress_piecewise_first, color = 'yellow')
plt.plot(x_line_maxStress_peicewise_second, y_line_maxStress_piecewise, color = 'red')
plt.plot(x_line_maxStress, y_line_maxStress_single, color = 'black')
plt.legend(['Uniaxial Tension FlowCurve',  'Piecewise function (small strain)', 'Piecewise function (large strain)','Single function'])
plt.xlabel("True Strain")
plt.ylabel("True Stress")
plt.title("Fitted Swift Voce curve")
plt.savefig('Fitted Swift Voce curve (TD)')


plt.figure(3)
plt.scatter(X,Y)
x_line_maxStress = np.arange(0, 0.2, 0.001)
x_line_maxStress_peicewise_second = np.arange(0.022, 0.2, 0.001)
x_line_maxStress_peicewise_first = np.arange(0, 0.022, 0.001)

y_line_maxStress_piecewise = swiftVoce(x_line_maxStress_peicewise_second, a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2)
y_line_maxStress_single = swiftVoceT(x_line_maxStress, a, b, c, d, e, f, g)
y_line_maxStress_piecewise_first = swiftVoceT(x_line_maxStress_peicewise_first, a, b, c, d, e, f, g)

plt.plot(x_line_maxStress_peicewise_first, y_line_maxStress_piecewise_first, color = 'yellow')
plt.plot(x_line_maxStress_peicewise_second, y_line_maxStress_piecewise, color = 'red')

plt.legend(['Diagonal Direction FlowCurve',  'Piecewise function (small strain)', 'Piecewise function (large strain)','Single function'])
plt.xlabel("True Strain")
plt.ylabel("True Stress")
plt.title("Optimised Swift Voce")
plt.savefig('Optimised Swift Voce (TD)')



plt.show()

with open('parameters_piecewise.csv', 'w') as f:
    writer = csv.writer(f)
    ee= e
    ps1 =[a,b,c,d,ee,f,g]
    ps2 =[a1,b1,c1,d1,e1,f1,g1]
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
    j = 0
    for i in y_line_extend_piecewise_first:
        writer.writerow([y_line_extend_single_first[j]])
        j+=1
    j=0
    for i in y_line_extend_piecewise_second:
        if(i <=0.02):
            writer.writerow([y_line_extend_single_second[j]])
        else:
            writer.writerow([i])
        j+=1
    for i in y_line_extend_piecewise_third:
        writer.writerow([i])
