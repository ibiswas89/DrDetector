from scipy.spatial import distance
import dlib
import cv2
import numpy as np
import imutils
from imutils import face_utils
def eye_aspect_ratio(eye):
    V1 = distance.euclidean(eye[1],eye[5])
    V2 = distance.euclidean(eye[2],eye[4])
    H =  distance.euclidean(eye[0], eye[3])
    AR = (V1+V2)/(2*H)
    return AR

cap = cv2.VideoCapture(0)
cnt = 0 
predictor_path = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

while True:
	ret,frame = cap.read()
	#cap.stop()
        
	img = frame
	rects =detector(img,0)
        for rect in rects:
            cv2.rectangle(img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,255,0),3)
	    shape = predictor(img,rect)
	    shape = face_utils.shape_to_np(shape)
	    leftEye = shape[lStart:lEnd]
	    leftEyeHull = cv2.convexHull(leftEye)
	    rightEye = shape[rStart:rEnd]
            rightEyeHull = cv2.convexHull(rightEye)
 
	    LAR = eye_aspect_ratio(leftEye)
	    RAR = eye_aspect_ratio(rightEye)
            AAR = (LAR+RAR)/2
             
	    cv2.drawContours(frame,[leftEye],-1, (0,255,10), 1)
            cv2.drawContours(frame,[rightEye],-1, (0,255,10), 1)
            print AAR 
            if AAR < 0.27:
                cv2.putText(frame, "****************ALERT!****************", (10, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
	#print np.shape(shape)
        
	   # op_path= "output/output" + str(cnt) +".jpg"
        
        cv2.imshow("Frame", frame) 
	   # cv2.imwrite(op_path,frame)
           # cnt =cnt+1
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
 
 


