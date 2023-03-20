import smtplib
import time
import imaplib
import email

import os
import random
from email.header import Header, decode_header, make_header

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

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
        # Out: list of "folders" aka labels in gmail.

        result, data = mail.search(None, "ALL")

        ids = data[0] # data is a list.
        id_list = ids.split() # ids is a space separated string
        latest_email_id = id_list[-1] # get the latest
        

        result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

        raw_email = data[0][1] # here's the body, which is raw text of the whole email
        # including headers and alternate payloads

        #print raw_email

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
                #print payload.get_payload()
                #return x
                break
        else:
            print b.get_payload()
            #return b.get_payload()

        '''#continue inside the same for loop as above
        raw_email_string = raw_email.decode('utf-8')
        # converts byte literal to string removing b''
        email_message = email.message_from_string(raw_email_string)
        # this will loop through all the available multiparts in mail
        for part in email_message.walk():
            if part.get_content_type() == "text/plain": # ignore attachments/html
                body = part.get_payload(decode=True)
                x = str(body)
                save_string = str("D:Dumpgmailemail_" + str(x) + ".eml")
                # location on disk
                myfile = open(save_string, 'a')
                myfile.write(str(body))
                # body is again a byte literal
                myfile.close()
            else:
                continue'''

        '''email_message = email.message_from_bytes(b[0][1])  # converts raw email to email object

        parsed_dict = {
            'from': email.utils.parseaddr(email_message['From']),
            'to': email_message['To'],
            'subject': email_message['Subject'],
            'body_plain': '',
            'body_html': '',
            'attachments': []
        }

        for part in email_message.walk():  # iterates trough all parts of the email
            filename = part.get_filename()

            if bool(filename):  # if the part is actually an attachment, it will be True
                path = os.path.join(storage_path, filename)
                while os.path.isfile(path):  # while filename is already in use, try adding a random digit
                    filesplit = filename.split('.')
                    filename = filesplit[0] + '_' + str(random.randint(0, 99)) + '.' + filesplit[1]
                    path = os.path.join(storage_path, filename)

                fp = open(path, 'wb')  # open/create attachment file
                parsed_dict['attachments'].append(filename)
                fp.write(part.get_payload(decode=True))
                fp.close()

            else:
                if part.get_content_type() == 'text/plain':  # save plain text email body
                    parsed_dict['body_plain'] = part.get_payload(decode=True).decode('utf-8')
                elif part.get_content_type() == 'text/html':  # save html email body
                    parsed_dict['body_html'] = part.get_payload(decode=True).decode('utf-8')

        print parsed_dict'''

    except Exception, e:
        print str(e)


    a="accept" #new line is not the cause for inequality
    x.lower()
    if a in x:
        print "true"
    else:
        print "false"

read_email_from_gmail()

'''
# -------------------------------------------------
#
# Utility to store email parts in a dictionary
#
# ------------------------------------------------

def parse(email_b, storage_path='./attachments'):
    # email_b = binary email (b'...'), storage_path = relative or absolute path to store attachments
    email_message = email.message_from_bytes(email_b[0][1])  # converts raw email to email object

    parsed_dict = {
        'from': email.utils.parseaddr(email_message['From']),
        'to': email_message['to'],
        'subject': email_message['Subject'],
        'body_plain': '',
        'body_html': '',
        'attachments': []
    }

    for part in email_message.walk():  # iterates trough all parts of the email
        filename = part.get_filename()

        if bool(filename):  # if the part is actually an attachment, it will be True
            path = os.path.join(storage_path, filename)
            while os.path.isfile(path):  # while filename is already in use, try adding a random digit
                filesplit = filename.split('.')
                filename = filesplit[0] + '_' + str(random.randint(0, 99)) + '.' + filesplit[1]
                path = os.path.join(storage_path, filename)

            fp = open(path, 'wb')  # open/create attachment file
            parsed_dict['attachments'].append(filename)
            fp.write(part.get_payload(decode=True))
            fp.close()

        else:
            if part.get_content_type() == 'text/plain':  # save plain text email body
                parsed_dict['body_plain'] = part.get_payload(decode=True).decode('utf-8')
            elif part.get_content_type() == 'text/html':  # save html email body
                parsed_dict['body_html'] = part.get_payload(decode=True).decode('utf-8')

    return parsed_dict

parse(read_email_from_gmail())'''
