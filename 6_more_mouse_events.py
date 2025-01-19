import cv2
import numpy as np

def mouseCallback(event, x, y, flags, param):
    # Connecting lines
    # if(event == cv2.EVENT_LBUTTONDOWN):
    #     cv2.circle(img, (x,y), 5, (255,255,0), -1)
    #     points.append((x,y))

    #     if(len(points) >= 2):
    #         cv2.line(img, points[-1], points[-2], (0,255,0), 2)

        # cv2.imshow("image", img)

    # Showing color in different window
    if(event == cv2.EVENT_LBUTTONDOWN):
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        cv2.circle(img, (x,y), 5, (255,255,0), -1)
        my_color = np.zeros((512, 512, 3), dtype=np.uint8)
        my_color[:] = [blue, green, red]

        cv2.imshow("color window", my_color)

# img = np.zeros((512, 512, 3), dtype=np.uint8)
img = cv2.imread('files/lena.jpg')
cv2.imshow("image", img)
points = []
cv2.setMouseCallback("image", mouseCallback)

cv2.waitKey(0)
cv2.destroyAllWindows()
