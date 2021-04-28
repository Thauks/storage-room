import cv2
import time

cap = cv2.VideoCapture(0)

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 25, (int(cap.get(3)),int(cap.get(4))))

while True:
    
    l, frame = cap.read()
    cv2.imshow('test', frame)
    out.write(frame)
    key = cv2.waitKey(1)

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)

    if key == ord('p'):
         break

cap.release()
out.release()

cv2.destroyAllWindows()