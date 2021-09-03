#https://medium.com/@thejackmccumber/fetching-venmo-payment-details-using-python-3-and-gmail-85d20c76938a
import imaplib
import email
import pdb
import yaml
from datetime import datetime
import re

def getVenmoPaymentDetails():
    #load email login info
    email_info = None
    with open("secure_info.yaml", "r+") as yaml_file:
        email_info = yaml.safe_load(yaml_file)['venmo-email']
    #setup the email port and give permission details
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_info['address'], email_info['password'])
    mail.list()
    mail.select('inbox')


    #combs through inbox folders for the latest email
    result, data = mail.uid('search', None, "ALL")
    highest_recieved_uid = 6
    i = len(data[0].split())
    for x in range(highest_recieved_uid, i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = email_data[0][1]
     
    #get data from all unprocessed emails

        raw_email_string = raw_email.decode('utf-8')
        if "venmo" not in raw_email_string:
            continue
        email_message = email.message_from_string(raw_email_string)
        print("new email")
        print(email_message['Date'])
        for part in email_message.walk():
            if part.get_content_type() == "text/html": # ignore attachments/html
                pdb.set_trace()
                body = part.get_payload(decode=True)
                body = str((body.decode('utf-8')))

                cleanhtml = re.compile("<.*?>")
                body = re.sub(cleanhtml, '', body)

                lines = [l.lstrip() for l in body.split('\n')]
                lines = list(filter(None, lines))
                pdb.set_trace()
                if len(lines) < 10: 
                    continue
                relative_index = lines.index('paid\r')
                payee_line_relative = -1
                description_line_relative = 4
                date_amount_line_relative = 8
                #index from 'paid\r' for consistency
                #line 9 payee
                #date and amount on 17th line
                #line 15 description of payment
                payee = lines[relative_index + payee_line_relative].strip()
                description_raw = lines[relative_index + description_line_relative]
                date_amount_raw = lines[relative_index + date_amount_line_relative]
                recieved_date = ' '.join(email_message['Date'].split(' ')[0:-1])
                pdb.set_trace()
                date_obj = datetime.strptime(recieved_date, "%a, %d %b %Y %H:%M:%S").timestamp()
                dollar_amount = date_amount_raw[date_amount_raw.index('$')+1:date_amount_raw.index('\r')]

                
                pdb.set_trace()
                break


getVenmoPaymentDetails()