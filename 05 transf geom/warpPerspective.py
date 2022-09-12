import cv2
import matplotlib.pyplot as plt
import numpy as np

img1 = cv2.cvtColor(cv2.imread('livro.jpg'), cv2.COLOR_BGR2RGB)

img2 = cv2.warpPerspective(img1, np.array([[2, 0, 40],[0, 1, 90],[0.009, 0, 1]]).astype(np.float32), (300, 300))

plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.subplot(1, 2, 2)
plt.imshow(img2)
plt.show()

