import cv2 as cv
import winsound
import numpy as np

def motionDetection():
    capture = cv.VideoCapture('C:/Users/Linh/Documents/Opencv/Photos/Road.mp4')
    #capture = cv.VideoCapture(0)
    move_counter =0
    while True:
         _,frame1 = capture.read()
         _,frame2 = capture.read()
    # Diffrence of of both frame,== 0 if no change in both frame Ex: (145-145 = 0)
         motion = cv.absdiff(frame1,frame2)
         cv.imshow("doasmdoasdm",motion)
         grayFrame = cv.cvtColor(motion,cv.COLOR_BGR2GRAY)
         Blur = cv.GaussianBlur(grayFrame,(5,5),0)
     #threshold the frame
         _,thresh= cv.threshold(Blur,20,255,cv.THRESH_BINARY)
   # Dilation of the thresh
         dilation = cv.dilate(thresh,None,iterations=3)

    #find the contours(Boundry of the object)
         contour, hierarchies = cv.findContours(dilation, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
         for c in contour:

            if  cv.contourArea(c) < 10000:
                continue

        # get the x,y,w,h of the contour
            x,y,w,h = cv.boundingRect(c)
        # Draw a rectangle around the contour
            cv.rectangle(frame2,(x,y),(x+w, y+h), (0,255,0), 2)
            cv.putText(frame2, "Object Move", (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), thickness=1)

            move_counter +=1
            #winsound.Beep(1000,30)

         #cv.imshow('Motion Detected',cv.resize(frame2,(0,0),fx=2,fy=2))
         cv.imshow('Motion Detected',frame2)

         if cv.waitKey(30) == ord('q'):
             break

    print("Movement Detected",move_counter)

    capture.release()
    cv.destroyAllWindows()