'''Python's email package contains many classes and functions for composing and
parsing email messages.'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#compose some of the basic message headers

fromaddr = "kp.komalparikh1@gmail.com"
toaddr = "kp.komalparikh7@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"

#attach the body of the email to the MIME message

body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

'''For sending the mail, we have to convert the object to a string, and then
use the same prodecure to send using the SMTP server'''

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("kp.komalparikh1", "komalparikh1*")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
