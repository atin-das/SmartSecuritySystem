import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    #text = message.as_string()
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

sendemail(from_addr = 'kp.komalparikh1@gmail.com',
          to_addr_list = ['kp.komalparikh7@gmail.com'],
          cc_addr_list = [],
          subject = 'Howdy',
          message = 'Howdy from a python function',
          login = 'kp.komalparikh1@gmail.com',
          password = 'komalparikh1*')
