import math
import numpy as np
from matplotlib import pyplot as plt


#r = float(input("Enter parameter value: "))

def f(x):
	return x*(1-x)(-1-2*x)


steps = 1000
h = 0.01
xf = xi + h*steps
x1 = np.linspace(-2.0,2.0,25)
x = [0.0 for i in range(steps+2)]
t = [i for i in range(steps+2)]

x[0] = xi

for t in range(0,steps+1):
	#if x[t] > 10 or x[t] < -10 or y[t] > 10 or y[t] < -10 or z[t] > 10 or z[t] < -10 :
		#break
	j0 = f(x[t])
	j1 = f(x[t] + 0.5*j0*h)
	j2 = f(x[t] + 0.5*j1*h)
	j3 = f(x[t] + j2*h)
	j = (j0 + 2*j1 + 2*j2 + j3)/6
	x[t+1] = x[t] + j*h
	

fig,ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x1,f(x1))
plt.show()
fig,ax = plt.subplots()
plt.title("PT for x(0) = "+str(xi))
plt.xlabel('t')
plt.ylabel('x')
plt.plot(t,x)
plt.show()

