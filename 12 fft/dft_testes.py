#interpola a funcao
#2m eh a quantidade de pontos utilizada

import math
import matplotlib.pyplot as plt
import sys

m = int(sys.argv[1])
pts_x = []
pts_y = [3 for i in range(2*m)]

for i in range(0, 2*m):
    pts_x.append(-math.pi+i*math.pi/m)

#adiciona um pico suave
if True:
	pts_y[3] = 4
	pts_y[4] = 5.5
	pts_y[5] = 8
	pts_y[6] = 10
	pts_y[7] = 8
	pts_y[8] = 5.5
	pts_y[9] = 4
#adiciona um pico abrupto
if True:
	pts_y[20] = 10

#calcula a DFT
a = []
b = []
for k in range(0, m+1):
    somaA = 0
    somaB = 0
    for j in range(0, 2*m):
        somaA += pts_y[j]*math.cos(k*pts_x[j])
        somaB += pts_y[j]*math.sin(k*pts_x[j])
    a.append(somaA/m)
    if k != 0 and k != m:
        b.append(somaB/m)

x = []
y = []
for i in range(500):
	x_i = -15+30*i/500
	x.append(x_i)

	soma = a[0]/2 + a[m]/2*math.cos(m*x_i)
	for j in range(1, m):
# descarta as 14 ultimas frequencias mais altas
#		if j > m-14:
#			continue
		soma += a[j]*math.cos(j*x_i) + b[j-1]*math.sin(j*x_i)
	y.append(soma)

plt.plot(x, y, color='gray',zorder=1)
plt.scatter(pts_x, pts_y, zorder=2)

plt.xlim(-2*math.pi,2*math.pi)
plt.ylim(-1, 12)
plt.show()

