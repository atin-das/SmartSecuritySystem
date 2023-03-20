import smtplib
import time
import imaplib
import email
import os
import random
from email.header import Header, decode_header, make_header

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
                #print "final"
                #print x
                break
        else:
            print b.get_payload()
            
    except Exception, e:
        print str(e)

    x.lower()
    if "accept" in x or "allow" in x or "yes" in x:
        print "true"
    else:
        print "false"

read_email_from_gmail()
