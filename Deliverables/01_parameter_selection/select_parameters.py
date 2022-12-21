import random as random
from datetime import datetime

random.seed(datetime.now())

def randRange(a,b):
    return a+(random.random())*(b-a)
    

#damage parameters
d1 = []
d2 = []
d3 = []
d4 = []

bounds = [0.0001, 1, 2, 3]

def fixThreeFindOne(d, df1, df2, df3):
    fixed = randRange(0.0001, 3)
    for i in range(0,3):
        for j in range(0,2):
            d.append(randRange(bounds[i], bounds[i+1]))
            df1.append(randRange(0.0001, 3))
            df2.append(randRange(0.0001, 3))
            df3.append(randRange(0.0001, 3))

fixThreeFindOne(d1, d2, d3, d4)
fixThreeFindOne(d2, d1, d3, d4)
fixThreeFindOne(d3, d2, d1, d4)
fixThreeFindOne(d4, d2, d3, d1)
        
out = open('parameters.csv',mode='w')
for i in range(1, len(d1)):
    out.write(f"{d1[i]:.3f}, {d2[i]:.3f}, {d3[i]:.3f}, {d4[i]:.3f}\n")

out.close()

