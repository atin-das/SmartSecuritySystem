"""The first step is to create an SMTP object, each object is used for connection 
with one server."""
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.ehlo()
server.starttls()
server.login("kp.komalparikh1@gmail.com", "komalparikh1*")

#Send the mail
msg = "Hello! Email testing"
#The /n separates the message from the headers
server.sendmail("kp.komalparikh1@gmail.com", "kp.komalparikh7@gmail.com", msg)
