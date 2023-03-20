import email
import os
import random


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
