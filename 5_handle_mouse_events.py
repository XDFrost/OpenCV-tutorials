import cv2
import numpy as np

def mouseCallback(event, x_coordinate, y_coordinate, flags, params):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("X:", x_coordinate, " ", "Y:", y_coordinate)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = f"X: {x_coordinate}, Y: {y_coordinate}"
        cv2.putText(img, strXY, (x_coordinate,y_coordinate), font, .5, (0,255,255), 2)
        cv2.imshow("IMAGE WINDOW", img)
    
    if(event == cv2.EVENT_RBUTTONDOWN):
        blue = img[y_coordinate, x_coordinate, 0]
        green = img[y_coordinate, x_coordinate, 1] 
        red = img[y_coordinate, x_coordinate, 2] 
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = f"{blue}, {green}, {red}"
        cv2.putText(img, strXY, (x_coordinate, y_coordinate), font, .5, (255,255,0), 2)
        cv2.imshow("IMAGE WINDOW", img)

# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('files/lena.jpg')
cv2.imshow("IMAGE WINDOW", img)

cv2.setMouseCallback("IMAGE WINDOW", mouseCallback)         
cv2.waitKey(0)
cv2.destroyAllWindows()