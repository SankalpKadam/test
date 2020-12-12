# import the opencv library 
import cv2 

# define a video capture object 
vid = cv2.VideoCapture(0) 
while(True):
    ret, frame = vid.read() 
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    if len(faces) :
        print("Found {0} faces!".format(len(faces)))
    
    # Draw a rectangle around the faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(127,0,255),2)
    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
