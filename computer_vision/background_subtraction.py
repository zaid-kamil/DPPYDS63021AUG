# pip install opencv-contrib-python
import cv2

bgmask = cv2.createBackgroundSubtractorKNN()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret:
        fgmask = bgmask.apply(frame)
        cv2.imshow('window', frame)
        cv2.imshow('masked image', fgmask)
        if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()