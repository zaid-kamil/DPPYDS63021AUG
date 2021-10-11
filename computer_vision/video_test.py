# pip install opencv-contrib-python
import cv2

cap = cv2.VideoCapture("c:/users/HP 346 G3/Videos/drawing.mkv")
while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('window', frame)
        if cv2.waitKey(1) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
