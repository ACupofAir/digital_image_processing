# 均值滤波
#%%
import numpy as np
import cv2

#%% cv2自带的均值滤波
img_org = cv2.imread("../images/sample.jpg")
cv2.imshow("img_org", img_org)

img_blur = cv2.blur(img_org, (20, 20))
cv2.imshow("img_blur", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
#%% 手动实现均值滤波
def mean_filter(img, kernel_size: int):
    # 高，宽，信道（rgb）
    h, w, c = img.shape

    pad = kernel_size // 2
    out = np.zeros((h + 2 * pad, w + 2 * pad, c), dtype=np.float32)
    out[pad : pad + h, pad : pad + w] = img.copy().astype(np.float32)

    tmp = out.copy()
    for y in range(h):
        for x in range(w):
            for ci in range(c):
                out[pad + y, pad + x, ci] = np.mean(
                    tmp[y : y + kernel_size, x : x + kernel_size, ci]
                )

    out = out[pad : pad + h, pad : pad + w].astype(np.uint8)

    return out


#%%

img_mine_meanfilter = mean_filter(img_org, 20)
cv2.imshow("mine_blur", img_mine_meanfilter)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
