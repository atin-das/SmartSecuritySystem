import cv2
import os
import numpy as np
from PIL import Image
import smtplib
import imaplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
#from final import *

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
#rec=cv2.createLBPHFaceRecognizer()
#rec=cv2.face.LBPHFaceRecognizer_create()
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read('recognizer/trainingdata.yml')
# load() is replaced with read() and save() is replaced with write()
id=0

strFrom = 'kp.komalparikh1@gmail.com'
strTo = 'kp.komalparikh7@gmail.com'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Test message'
msgRoot['From'] = 'kp.komalparikh1@gmail.com'
msgRoot['To'] = 'kp.komalparikh7@gmail.com'
msgRoot = MIMEMultipart('mixed')

'''path='dataSet'
imagePaths=[os.path.join(path,f) for f in os.listdir(path)]'''

#font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
#font = (cv2.FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==1):
            id="Komal"
            '''user_id=""
            for imagePath in imagePaths:
                #faceImg=Image.open(imagePath).convert('L');
                #print imagePath
                user_id=user_id.join(imagePath.split('.')[1:2])
                print user_id
                if user_id == 1:
                    fp = open(imagePath, 'rb')
                    imgtosend = MIMEImage(fp.read())
                    fp.close()
                    msgRoot.attach(imgtosend)
                    #msgRoot.attach(faceImg)
                else:
                    break'''
            '''s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
            s.sendmail(strFrom, strTo, "Komal has visited")
            s.quit()'''
        elif(id==2):
            id="Nirmalya"
            '''s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
            s.sendmail(strFrom, strTo, "Nirmalya has visited")
            s.quit()'''
        elif(id==3):
            id="Ankit"
            '''s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
            s.sendmail(strFrom, strTo, "Ankit has visited")
            s.quit()'''
        elif(id==4):
            id="Atin"
            '''s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
            s.sendmail(strFrom, strTo, "Atin has visited")
            s.quit()'''
        elif(id==5):
            id="Riyan"
            '''s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
            s.sendmail(strFrom, strTo, "Riyan has visited")
            s.quit()'''
        elif(id==6):
            id="Dipsa"
            '''s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
            s.sendmail(strFrom, strTo, "Dipsa has visited")
            s.quit()'''
        elif(id==7):
            id="Abhik"
            '''s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
            s.sendmail(strFrom, strTo, "Abhik has visited")
            s.quit()'''
        #cv2.cv.putText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255),2)
        #cv2.putText((img),str(id),(x,y+h),font,(0,0,255),2)
        cv2.putText(img,str(id),(x,y+h),font,1.0,(0, 0, 255),2)
        #cv2.putText(img, str(id), (x,y+h), font, 1.0, 255, 2, cv2.LINE_AA, False)
    cv2.imshow("Face",img)
    if(cv2.waitKey(1)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
