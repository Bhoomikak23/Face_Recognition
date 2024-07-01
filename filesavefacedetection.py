import cv2
import random

cam=cv2.VideoCapture(0)



cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  #features extract 

crop=""
while True:
    flag,imag=cam.read()
    gray=cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
    faces=cascade.detectMultiScale(gray,1.1,5)

    print(faces)

    for x,y,w,h in faces:
        cv2.rectangle(imag,(x,y),(x+w,y+h),(255,255,0),2)
        crop=imag[y:y+h,x:x+w]

        crop=cv2.resize(crop,(300,300))
        


    cv2.imshow("myimage",imag)
    k=cv2.waitKey(1)
    
    if k==ord('q'):
        break
    if k==ord('s'):
        index=random.randint(1,100)
        filename=f"./dataset/3/cropped{index}.jpg"
        cv2.imwrite(filename,crop)
cam.release()