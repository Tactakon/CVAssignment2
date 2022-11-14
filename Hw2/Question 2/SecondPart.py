import numpy as np
import cv2

imgPath1=["Test1/1Left.jpg","Test1/1Middle.jpg","Test1/1Right.jpg"]

imgPath2=["Test2/2Left.jpg","Test2/2Middle.jpg","Test2/2Right.jpg"]

imgPath3=["Test3/3Left.jpg","Test3/3Middle.jpg","Test3/3Right.jpg"]

imgPath4=["Test4/4Left.jpg","Test4/4Middle.jpg","Test4/4Right.jpg"]

imgPath5=["Test5/5Left.jpg","Test5/5Middle.jpg","Test5/5Right.jpg"]

images = []

for path in imgPath5:
	image = cv2.imread(path)
	images.append(image)

print(len(images))
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	print("Image Stitching Successful")
	cv2.imshow("Stitched Image", stitched)
	cv2.imwrite("stitchedimg5.png", stitched)
	cv2.waitKey(0)
else:
	print("[INFO] Failed Image Stitching ({})"/format(status))
