import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

while(cap.isOpened()):
    ret, frame = cap.read()
    if(ret == True):
        font = cv2.FONT_HERSHEY_SIMPLEX
        # text = 'Width:' + str(width) + ' Height:' + str(height)
        dateT = datetime.now()

        # Writing text on video
        # frame = cv2.putText(frame, text, (50,150), font, 2, (0,255,255), 3, cv2.LINE_AA)
        frame = cv2.putText(frame, str(dateT), (50,150), font, 2, (0,255,255), 3, cv2.LINE_AA)

        cv2.imshow("IMAGE WINDOW", frame)

        if(cv2.waitKey(1) == ord('s')):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
