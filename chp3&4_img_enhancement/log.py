#%%
from cmath import log
import numpy as np
import sys

sys.path.append("..")
sys.path.append(".")
from utils import *

#%%
def log_image(img, c=1):
    """
    对数变换，计算公式为 s = c*log(1+l)
    """
    output = c * np.log(1.0 + img)
    return output


#%%
if __name__ == "__main__":
    s = visualization(1, 5)
    img = get_image("RGB", "../images/sample.jpg")
    img1 = log_image(img, c=4)
    img2 = log_image(img, c=8)
    img3 = log_image(img, c=16)
    img4 = log_image(img, c=32)
    s.append_img(img)
    s.append_img(img1)
    s.append_img(img2)
    s.append_img(img3)
    s.append_img(img4)
    s.show()
# %%
