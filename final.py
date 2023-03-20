import RPi.GPIO as gpio
import picamera
import time
import smtplib
import imaplib
import email
import os
import random
from email.header import Header, decode_header, make_header
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
 
fromaddr = "kp.komalparikh1@gmail.com"
toaddr = "kp.komalparikh7@gmail.com"

 
mail = MIMEMultipart()
 
mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Attachment"
body = "Please find the attachment" 
led=17
pir=18
HIGH=1
LOW=0
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(led, gpio.OUT)           # initialize GPIO Pin as output
gpio.setup(pir, gpio.IN)            # initialize GPIO Pin as input
data=""
def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    print (data)
    dat='%s.jpg'%data
    print (dat)
    attachment = open(dat, 'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    mail.attach(image)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("kp.komalparikh1@gmail.com", "komalparikh1*")
    text = mail.as_string()
    server.sendmail("kp.komalparikh1@gmail.com", "kp.komalparikh7@gmail.com", text)
    server.quit()
    return(1)
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "kp.komalparikh1" + ORG_EMAIL
FROM_PWD    = "komalparikh1*"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 587


def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        (retcode, capabilities) = mail.login('kp.komalparikh1@gmail.com','komalparikh1*')
        mail.list()
        mail.select('inbox')

        n=0
        (retcode, messages) = mail.search(None, '(UNSEEN)')
        print messages
        print len(messages)
        if retcode == 'OK':
           for num in messages[0].split() :
              print 'Processing '
              n=n+1
              typ, data = mail.fetch(num,'(RFC822)')
              for response_part in data:
                  print "in for"
                  if isinstance(response_part, tuple):
                      print "in if"
                      original = email.message_from_string(response_part[1])
                      print original['From']
                      print original['Subject']
                      typ, data = mail.store(num,'+FLAGS','\\Seen')
                      result, data = mail.fetch(num, "(RFC822)")
                      raw_email = data[0][1]
                      x=""
                      b = email.message_from_string(raw_email)
                      if b.is_multipart():
                          print "inside if of multipart"
                          for payload in b.get_payload():
                              x = x + str(payload.get_payload())
                              print x
                              x = '\n'.join(x.split('\n')[0:1])
                              print "final"
                              print x
                              break
                      else:
                          print b.get_payload()
        if messages[0] == '':
            print "No mail received"
            x="Empty mail"
                
    except Exception, e:
        print str(e)
 
    x.lower()
    if "accept" in x or "allow" in x or "yes" in x:
        print "true"
    else:
        print "false"

    if(n==0):
        return(0)
    else:
        return(1)

def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(5)
    print (data)
    camera.capture('%s.jpg'%data)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    time.sleep(1)
    if sendMail(data)==1:
        i=0
        while True:
            if read_email_from_gmail()==1:
                break
            else:
                time.sleep(5)
                i+=1
                if i==4: #for two minutes
                    break
    '''#print lat
    #new_latest = (int(lat[0])+1)
    #print new_latest
    #if(new_latest==latest[1]):
        #read_email_from_gmail()'''
gpio.output(led , 0)
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
while 1:
    if gpio.input(pir)==1:
        gpio.output(led, HIGH)
        capture_image()
        while(gpio.input(pir)==1):
            time.sleep(1)    
    else:
        gpio.output(led, LOW)
        time.sleep(0.01)
