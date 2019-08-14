import numpy as np
import cv2
import smtplib
import send_email

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

def faceDetection():
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Find faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Checks if face is detected; if so - take a picture
            if (x, y, w , h) != None:
                ramp_frames = 1

                def get_image():
                    retval, im = cap.read()
                    return im

                for i in xrange(ramp_frames):
                    get_image()

                camera_capture = get_image()
                file = "test_image.png"
                cv2.imwrite(file, camera_capture)
                # send_email.sendEmail(file)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__== "__main__":
    faceDetection()

