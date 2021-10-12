import cv2
import mediapipe as mp
import numpy as np

mp_draw = mp.solutions.drawing_utils
mp_ss = mp.solutions.selfie_segmentation

BG_COLOR = (20, 20, 20) 
cap = cv2.VideoCapture(0)
with mp_ss.SelfieSegmentation(
    model_selection=0) as selfie_segmentation:
    bg_image = cv2.imread('two.png')
  
  
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("😒")
            continue
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        results = selfie_segmentation.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > .1
        if bg_image is None:
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR
        else:
            bg_image = cv2.resize(bg_image,(image.shape[1],image.shape[0]))
        output_image = np.where(condition, image, bg_image)
        cv2.imshow('Meet', output_image)
        if cv2.waitKey(5) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()