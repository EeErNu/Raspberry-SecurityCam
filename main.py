import numpy as np
import cv2
import smtplib
import send_email

cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

def snapShot(x, y, w, h):
    if (x, y, w, h) != None:
        ramp_frames = 1

        def getImage():
            retval, image = cap.read()
            return image

        for i in xrange(ramp_frames):
            getImage()

        camera_capture = getImage()
        file = "test_image.png"
        cv2.imwrite(file, camera_capture)
        send_email.sendEmail(file)

def faceDetection():
    while(True):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            snapShot(x, y, w, h)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    faceDetection()

