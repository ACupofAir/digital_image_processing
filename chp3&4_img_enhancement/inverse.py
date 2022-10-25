#%%
import numpy as np
import sys

# import the module written self
sys.path.append("..")
from utils import *

#%%
test_util()


#%%
def image_inversion(img, L):
    print(img.shape)
    """
    反转图像的灰度值，计算公式为 s = L - 1 - img
    """
    m = (L - 1) - img.astype(np.float32)
    m = normalize_image(m)
    print(m.shape)
    return m


#%%
if __name__ == "__main__":
    s = visualization(1, 2)
    img = get_image("RGB", "../images/sample.jpg")
    img_inversed = image_inversion(img, 256)
    s.append_img(img)
    s.append_img(img_inversed)
    s.show()

# %%
