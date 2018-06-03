##Step 1 : Reading an image using python
           Using PIL(Pillow library) ;; 
           Code: 
               from PIL import Image
               jpgfile = Image.open("picture.jpg")          
           Using opencv
           Code:
               import cv2
               img = cv2.imread("picture.jpg")
###Step 2 : Convert Image to grey scale
            img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            
###Step 3 : Detecting facial landmarks
            Used to localize and represent salient regions of face
            Eg Eyes,Eyebrows,Nose,Mouth,Jawline
############ Substep 1 :Localize the face in image: Either use opencv HaarCascades or deep learning based algorithms for face localization
############ Substep 2: Detect key facial landmarks: 
                                                      
