import cv2
import numpy as np


def rescale_frame(frame, wpercent=130, hpercent=130):
    width = int(frame.shape[1] * wpercent / 100)
    height = int(frame.shape[0] * hpercent / 100)
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)

def main():
    capture = cv2.VideoCapture(0)

    while capture.isOpened():
        pressed_key = cv2.waitKey(1)
        _, frame = capture.read()
        frame = cv2.flip(frame, 1)

        cv2.imshow("Live Feed", rescale_frame(frame))

        if pressed_key == 27: # Press Esc to qui the video
            break
        
    cv2.destroyAllWindows()
    capture.release()




