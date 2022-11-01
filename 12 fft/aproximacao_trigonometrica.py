#aproxima a funcao pela serie de fourier
#2m eh a quantidade de pontos utilizada
#n eh a quantidade de senos/cossenos

import math
import matplotlib.pyplot as plt
import sys

def f(x):
    return x*x+3*x-4

m = int(sys.argv[1])
n = int(sys.argv[2])
pts_x = []
pts_y = []
for i in range(0, 2*m):
    pts_x.append(-math.pi+i*math.pi/m)
    pts_y.append(f(pts_x[i]))

a = []
b = []
for k in range(0, n+1):
	somaA = 0
	somaB = 0
	for j in range(0, 2*m):
		somaA += pts_y[j]*math.cos(k*pts_x[j])
		somaB += pts_y[j]*math.sin(k*pts_x[j])
	a.append(somaA/m)
	if k != 0:
		b.append(somaB/m)

x = []
y = []
for i in range(500):
#x_i = -math.pi+i*math.pi/250
	x_i = -15+30*i/500
	x.append(x_i)

	soma = a[0]/2
	for j in range(1, n+1):
		soma += a[j]*math.cos(j*x_i) + b[j-1]*math.sin(j*x_i)
	y.append(soma)

plt.plot(x, y, color='gray',zorder=1)
plt.scatter(pts_x, pts_y, zorder=2)

#plt.xlim(-math.pi,math.pi)
plt.xlim(-5*math.pi,5*math.pi)
plt.show()
