"""python facial recognition"""
import numpy
import cv2
from PIL import Image

"""opens up laptop webcam"""
frontface_path = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(frontface_path) #insert path here
vc = cv2.VideoCapture(0)

while True:
    rval, frame = vc.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,
    scaleFactor=1.2, minNeighbors = 2  #, flags= cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        circle_cord_x = int(x+ (w/2))
        circle_cord_y = int(y+ (h/2))

        #creates box aroundface
        box = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)

        #creates circle in center of box
        circle = cv2.circle(frame, (circle_cord_x,circle_cord_y),2,(255,0,0),1)


    #outputs video w/ box around detected face
    cv2.imshow('Output', frame)

    key = cv2.waitKey(10)
    if key == 27: #esc key closes window
        break
vc.release()
cv2.destroyAllWindows()
"""-----"""
