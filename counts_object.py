import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from scipy.ndimage import morphology

def count(image, mask):
  erosion = morphology.binary_erosion(image, mask)
  dilation = morphology.binary_dilation(erosion, mask)
  image -= dilation
  count = label(dilation).max()
  return count

image = np.load("C:\\progrpython\\img\\ps.npy.txt")

masks = np.array([
                  np.array([
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1]]),
                  np.array([
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1]]),
                  np.array([
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1],
                            [1, 1, 0, 0, 1, 1],
                            [1, 1, 0, 0, 1, 1]]),
                  np.array([
                            [1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 0, 0],
                            [1, 1, 0, 0],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]]),
                  np.array([
                            [1, 1, 1, 1],
                            [1, 1, 1, 1],
                            [0, 0, 1, 1],
                            [0, 0, 1, 1],
                            [1, 1, 1, 1],
                            [1, 1, 1, 1]])], dtype=object)

total_amount = 0
for mask in masks:
  amount = count(image, mask)
  total_amount += amount
  print(f'number of objects:', amount)
print('total number of objects:', total_amount)