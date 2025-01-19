import cv2

img = cv2.imread('files/messi5.jpg')

print(img.shape)
print(img.size) 
print(img.dtype)

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))        

cv2.imshow('image', img)
cv2.imshow('Blue channel', b) 
cv2.imshow('Green channel', g) 
cv2.imshow('Red channel', r) 
cv2.waitKey(0)
cv2.destroyAllWindows()