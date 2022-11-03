import cv2, numpy as np
import sys
import matplotlib.pyplot as plt

img = cv2.imread(sys.argv[1], 0)

filtro = np.zeros(img.shape)

#filtro da media tamanho M por M
M = 20
filtro[0:M,0:M] = 1.0/(M*M)

F = np.fft.fft2(filtro, s=(512, 512))
I = np.fft.fft2(img, s=(512, 512))

F = np.fft.fftshift(F)
I = np.fft.fftshift(I)
res = np.multiply(F, I)

espectroF = 20*np.log(np.abs(F)**2)
espectroI = 20*np.log(np.abs(I)**2)
espectroRes = 20*np.log(np.abs(res)**2)

img_back = np.fft.ifft2(np.fft.fftshift(res))
img_back = img_back[0:img.shape[0],0:img.shape[1]]

plt.subplot(3,2,1),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,2),plt.imshow(espectroI, cmap = 'gray')
plt.title('Espectro da Imagem'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,3),plt.imshow(filtro, cmap = 'gray')
plt.title('Filtro'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,4),plt.imshow(espectroF, cmap = 'gray')
plt.title('Espectro do Filtro'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,5),plt.imshow(espectroRes, cmap = 'gray')
plt.title('Espectro do produto Imagem Filtro'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,6),plt.imshow(img_back.astype(np.uint8), cmap = 'gray')
plt.title('Inversa'), plt.xticks([]), plt.yticks([])
plt.show()

