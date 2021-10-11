import cv2

img = cv2.imread('two.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img4 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('imagewindow', img)
cv2.imshow('imagewindow2', img2)
cv2.imshow('imagewindow3', img3)
cv2.imshow('imagewindow4', img4)
print(img.shape)
# resized to 100x100
img100100 = cv2.resize(img, (100, 100))
# resized to half size
imghalf = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

cv2.imshow('100x100', img100100)
cv2.imshow('halved', imghalf)
cv2.waitKey(0)