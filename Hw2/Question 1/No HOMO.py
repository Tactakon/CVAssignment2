import cv2
import numpy as np
import matplotlib.pyplot as plt

src_points = np.array([[447,274],[191,294],[194,110],[382,117],[298,175] ])
dest_points = np.array([[429,386],[192,416],[369,205],[174,213],[284,304]])


h, status = cv2.findHomography(src_points, dest_points)
print(h)
im_src = cv2.imread('Za 1.png')
im_dst = cv2.imread('Za 2.png')

im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

cv2.imshow("Warped_Source_Image", im_out)
plt.imshow(im_out)
plt.show()

#Coordinates for Left
# 447   274
# 191   294
# 194   110
# 382   117
# 298   175

#Coordinates for Middle
# 429   386
# 192   416
# 369   205
# 174   213
# 284   304


