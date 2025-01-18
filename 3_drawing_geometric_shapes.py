import cv2

img_path = "files/lena.jpg"
img = cv2.imread(img_path, 1)

# Drawing line
img = cv2.line(img, (0,0), (255,255), (0, 0, 255), 5) 

# Drawing a arrow
img = cv2.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 5) 

# Drawing rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0,0,255), -1)

# Drawing circle
img = cv2.circle(img, (447, 63), 63, (0,255,0), -1)

# Adding text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OPENCV', (10,500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("Image Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
