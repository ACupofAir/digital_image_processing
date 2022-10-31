#%%
import cv2
import time
from matplotlib import pyplot as plt
from numpy import number

#%%
"""
这里重新设置图片大小
args:
   org_img: 要处理的图片路径
   zoom_ratio: 缩放的倍率
   output_name: 处理后存放的路径
"""


def resize_img(org_img_path, zoom_ratio: float, resized_img_path=''):
    org_img = cv2.imread(org_img_path)
    new_height = int(org_img.shape[0] * zoom_ratio)
    new_width = int(org_img.shape[1] * zoom_ratio)

    if not resized_img_path:
        resized_img_path = "resize_img"
        resized_img_path += time.strftime(
            "%Y-%m-%d-%H_%M_%S", time.localtime(time.time())
        )
        resized_img_path += ".jpg"

    resize_img = cv2.resize(
        org_img, (new_width, new_height), interpolation=cv2.INTER_AREA
    )

    cv2.imwrite(resized_img_path, resize_img)
    print("File saved in: ", resized_img_path)


#%%
resize_img("../images/sample.jpg", 1.5, "../resized_img.jpg")

# %%
