#%%
import numpy as np
import sys
import cv2

sys.path.append("..")
sys.path.append(".")
from utils import *
import matplotlib.pyplot as plt


# %% 直方图均衡化opencv实现
img_org = cv2.imread("../images/sample.jpg", 0)
img_cv = cv2.equalizeHist(img_org)
cv2.imshow("org_image", img_org)
cv2.waitKey(0)
cv2.imshow("hist_image", img_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%% 从零实现的直方图均衡化
hist, bins = np.histogram(img_org.ravel(), 256, [0, 256])

cdf = np.cumsum(hist)  # 计算累积函数值
cdf_normalized = cdf * max(hist) / max(cdf)

#%%
# 构建 Numpy 掩模数组，cdf 为原数组，当数组元素为 0 时，掩盖（计算时被忽略）。
cdf_m = np.ma.masked_equal(cdf, 0)

# 均衡化公式
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())

# 对被掩盖的元素赋值，这里赋值为 0
cdf = np.ma.filled(cdf_m, 0).astype("uint8")

img_np_hist = cdf[img_org]
#%% 处理前后图片对比
cv2.imshow("Before equal", img_org)
cv2.waitKey(0)
cv2.imshow("After equal", img_np_hist)
cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
hist2, bins2 = np.histogram(img_np_hist.ravel(), 256, [0, 256])

cdf2 = np.cumsum(hist2)
cdf_equal_normalized = cdf2 * max(hist2) / max(cdf2)
#%% 处理前后直方图对比

plt.subplot(121)
plt.plot(cdf_normalized, color="r")
plt.hist(img_org.ravel(), 256, [0, 256])  # type: ignore
plt.legend(("cdf", "histogram"), loc="upper left")
plt.title('org_image')
plt.subplot(122)
plt.hist(img_np_hist.ravel(), 256, [0, 256])  # type: ignore
plt.plot(cdf_equal_normalized, "r")
plt.legend(("cdf", "histogram"), loc="upper left")
plt.title('hist_image')
plt.show()
# %%
