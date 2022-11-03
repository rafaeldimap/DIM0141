import numpy as np, cv2, math
import sys
import matplotlib.pyplot as plt
import random

img = cv2.imread(sys.argv[1], 0)
H, W = img.shape

F = np.fft.fftshift(np.fft.fft2(img, (512, 512)))
G = F.copy()

d = 10
G[256-d,256-d] = 4500000
G[256+d,256+d] = 4500000

img_back = np.fft.ifft2(np.fft.fftshift(G))

espectroF = 20*np.log(np.abs(F))
espectroG = 20*np.log(np.abs(G))

plt.subplot(2,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Input Imagem'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(espectroF, cmap = 'gray')
plt.title('Espectro (shifted)'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(espectroG, cmap = 'gray')
plt.title('Espectro processado'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(img_back.astype(np.uint8), cmap = 'gray')
plt.title('Resultado'), plt.xticks([]), plt.yticks([])
plt.show()

