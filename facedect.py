import cv2
import time
campath = "haarcascade.xml"
facetrack = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#boot up camera
video_capture = cv2.VideoCapture(0)
#oh shit my pc fan is going insane o and now my pc booted off, oops
time.sleep(0.1)
#camera start record
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if int(cv2.__version__.split('.')[0]) >= 3:
        cv_flag = cv2.CASCADE_SCALE_IMAGE
    else:
        cv_flag = cv2.cv.CV_HAAR_SCALE_IMAGE
    faces = facetrack.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv_flag
    )
    #its great we have a face detect so lets show prove by prin- i mean draw funny rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
    #display the resulting image
    cv2.imshow('Video', frame)
	#AHHHH HELP ME LET ME GOO, Press z to quit transaction
    if cv2.waitKey(1) & 0xFF == ord('z'):
        break
#please let me leave!!!!
video_capture.release()
cv2.destroyAllWindows()