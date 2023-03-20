import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

strFrom = 'kp.komalparikh1@gmail.com'
strTo = 'kp.komalparikh7@gmail.com'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Test message'
msgRoot['From'] = 'kp.komalparikh1@gmail.com'
msgRoot['To'] = 'kp.komalparikh7@gmail.com'
msgRoot.preamble = 'This is a multi-part message in MIME format.'

'''msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)'''

msgAlternative = MIMEMultipart('mixed')
msgRoot = MIMEMultipart('mixed')

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

msgText = MIMEText('<b>Test HTML with Images</b><br><br>'
                   '<img src="cid:o2">'
                   '<img src="cid:o3">' #multiple images in html not working
                   '<img src="cid:o4">' #only one image displayed in html
                   '<img src="cid:o4">' #but attachments are working fine
                   '<br>'
                   'Sending Four Attachments', 'html')

msgAlternative.attach(msgText)

fp = open('o2.jpg', 'rb')
msgImage1 = MIMEImage(fp.read())
fp.close()
msgImage1.add_header('Content-ID', '<o2>')
msgRoot.attach(msgImage1)

fp = open('o3.jpg', 'rb')
msgImage2 = MIMEImage(fp.read())
fp.close()
msgImage1.add_header('Content-ID', '<o3>')
msgRoot.attach(msgImage2)

fp = open('o4.jpg', 'rb')
msgImage3 = MIMEImage(fp.read())
fp.close()
msgImage1.add_header('Content-ID', '<o4>')
msgRoot.attach(msgImage3)

fp = open('o5.jpg', 'rb')
msgImage4 = MIMEImage(fp.read())
fp.close()
msgImage1.add_header('Content-ID', '<o5>')
msgRoot.attach(msgImage4)

msgRoot.attach(msgAlternative)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login('kp.komalparikh1@gmail.com', 'komalparikh1*')
s.sendmail(strFrom, strTo, msgRoot.as_string())
s.quit()
