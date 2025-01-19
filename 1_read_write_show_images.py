import cv2

img_path = "files/lena.jpg"

# read image

img = cv2.imread(img_path, 1)
print("\n\n", "IMAGE", "\n\n", img)

# show image

cv2.imshow("Image Window", img)
# cv2.waitKey(0)       
# cv2.destroyAllWindows()
k = cv2.waitKey(0)       

# write image 

# cv2.imwrite("OpenCV/written_Images/lena_copy.jpg", img)
if(k == 27):
    print("DESTROYED")
    cv2.destroyAllWindows()
elif(k == ord('s')):
    print("SAVED AND DESTROYED")
    cv2.imwrite("written_Images/saved_using_key.png", img)
    cv2.destroyAllWindows()
