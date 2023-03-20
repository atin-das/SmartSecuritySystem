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
def capture_image():
    data= time.strftime("%d_%b_%Y|%H:%M:%S")
    camera.start_preview()
    time.sleep(5)
    print (data)
    camera.capture('%s.jpg'%data)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    time.sleep(1)
    sendMail(data)
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

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "kp.komalparikh1" + ORG_EMAIL
FROM_PWD    = "komalparikh1*"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 587

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        print "mail inbox selected"

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        print first_email_id
        print latest_email_id


        for i in range(latest_email_id,first_email_id, -1):
            typ, data = mail.fetch(i, '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print 'From : ' + str(email_from) + '\n'
                    print 'Subject : ' + str(email_subject) + '\n'
        mail.list()
        result, data = mail.search(None, "ALL")
        ids = data[0]
        id_list = ids.split()
        latest_email_id = id_list[-1]
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1]
        x=""
        b = email.message_from_string(raw_email)
        if b.is_multipart():
            for payload in b.get_payload():
                # if payload.is_multipart(): ...
                x = x + str(payload.get_payload())
                print x
                x = '\n'.join(x.split('\n')[0:1])
                print "final"
                print x
                break
        else:
            print b.get_payload()
            
    except Exception, e:
        print str(e)

    x.lower()
    if "access" in x or "allow" in x or "yes" in x:
        print "true"
    else:
        print "false"

read_email_from_gmail()
