#interpola a funcao
#2m eh a quantidade de pontos utilizada

import math
import matplotlib.pyplot as plt
import sys
import numpy as np

if len(sys.argv)%2 == 0:
    print('Forneca um numero par de amostras')
    exit(-1)

m = (len(sys.argv)-1)//2
print(len(sys.argv)-1)
pts_x = []
pts_y = [float(sys.argv[i]) for i in range(1, len(sys.argv))]

for i in range(0, 2*m):
    pts_x.append(-math.pi+i*math.pi/m)


#calcula a DFT
a = []
b = []
c = []
#for k in range(0, m+1):
for k in range(0, 2*m+1):
    somaA = 0
    somaB = 0
    for j in range(0, 2*m):
        somaA += pts_y[j]*math.cos(k*pts_x[j])
        somaB += pts_y[j]*math.sin(k*pts_x[j])
    ca = somaA/m
    cb = somaB/m
    c.append((m/(-1)**k)*(ca+(1j)*cb))
    if k == 0 or k == m:
        ca /= 2
    a.append(ca)
    b.append(cb)

print('Coeficientes a: ')
print(a)
print('Coeficientes b: ')
print(b)

print('Coeficientes c: ')
print(f'Total: {len(c)}')
print(c)

print('Coeficientes FFT: ')
f = np.fft.fft(pts_y)
print(f'Total: {len(f)}')
print(f)

x = []
y = []
for i in range(500):
        x_i = -15+30*i/500
        x.append(x_i)

        soma = 0
        for j in range(0, m+1):
            soma += a[j]*math.cos(j*x_i) + b[j]*math.sin(j*x_i)
        y.append(soma)

plt.subplot(1,2,1)
plt.plot(x, y, color='gray',zorder=1)
plt.scatter(pts_x, pts_y, zorder=2)
plt.xlim(-4*math.pi,4*math.pi)
plt.ylim(-1, 12)

plt.subplot(1,2,2)
plt.xlim(-1,3*m+1)
plt.title('Espectro')
plt.plot(np.abs(np.array(c)),marker='o')

plt.show()

