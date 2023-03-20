#sending images via mail
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

#s = smtplib.SMTP('smtp.gmail.com', 587)

def SendMail(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    fromaddr = "kp.komalparikh1@gmail.com"
    toaddr = "kp.komalparikh7@gmail.com"
    msg['Subject'] = 'Image Testing'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    text = MIMEText("test")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
    s.sendmail(fromaddr, toaddr, msg.as_string())
    s.quit()

SendMail('o1.jpg')
print "Done"
