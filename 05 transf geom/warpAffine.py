import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.cvtColor(cv2.imread('patch02.jpg'), cv2.COLOR_BGR2RGB)
img2 = cv2.warpAffine(img1, np.array([[2, 0, 0],[0, 2, 0]]).astype(np.float32), (500, 300))
img3 = cv2.warpAffine(img2, np.array([[1, 0, 100],[0, 1, 0]]).astype(np.float32), (500, 300))

ax1 = plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.subplot(1, 2, 2, sharex=ax1, sharey=ax1)
plt.imshow(img3)
plt.show()

