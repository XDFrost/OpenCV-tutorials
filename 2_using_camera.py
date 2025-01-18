import cv2

# Capturing livestream through camera
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print(int(cv2.CAP_PROP_FRAME_HEIGHT))
print(int(cv2.CAP_PROP_FRAME_WIDTH))

# Capturing through a video
# cap = cv2.VideoCapture("files/Megamind.avi")
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter('written_files/camera_test_1.avi', fourcc, 20.0, (640, 480))        

while(cap.isOpened()):
    # Reading Frames
    ret, frame = cap.read()


    if(ret == True):
        # Grayscaling
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # writing colored vid
        out.write(frame)

        # cv2.imshow("Frame Window", frame)
        cv2.imshow("Frame Window", gray)
        if(cv2.waitKey(1) == ord('s')):
            break
    else:
        break

# Releasing resources
cap.release()
out.release()
cv2.destroyAllWindows()
