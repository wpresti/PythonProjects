import cv2
import sys
#read the image. first command line arg is image
image = cv2.imread(sys.argv[1])
cv2.imshow("Image", image)
cv2.waitKey(0)  #wait for a keypress to close image
