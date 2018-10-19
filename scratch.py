
import cv2
import numpy as np

#img = cv2.imread('C:\\Users\\Amir\\Desktop\\try1.bmp')
img=np.zeros((512,512,3),np.int8)
# cv2.imwrite('C:\\Users\\Amir\\Desktop\\try1.jpg',img)
# cv2.namedWindow('amir',cv2.WINDOW_AUTOSIZE)
# cv2.imshow('amir',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows('amir')
cv2.line(img,(0,100),(100,0),(255,0,0),10)
cv2.putText(img,'AMir',(100,100),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,127))
cv2.imshow('amin',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
print(type(img))
print(img.dtype)
print(img.shape)







