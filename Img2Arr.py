'''
Turn images into numpy arrays
'''

from PIL import Image
import numpy as np
import os

r_path = r"C:\Users\DELL\Desktop\valPics_gray"

res = []
for filename in os.listdir(r_path):
    im = Image.open(os.path.join(r_path, filename))
    arr = list(np.array(im))
    res.append(arr)
res = np.array(res)
print(res.shape)

np.save("Images.npy", res)