from skimage import io
import matplotlib.pyplot as plt

h500 = io.imread('https://via.placeholder.com/300.png')
plt.imshow(h500)

print(h500.shape)

plt.imshow(h500[:,::-1])
plt.imshow(h500[::-1])
plt.imshow(h500[::-1])

plt.imshow(h500[100:200, 100:250])
