import imaplib
import email
import yaml
import datetime
import re

from Payment import Payment


class PaymentProcessorException(Exception):
    pass

class PaymentProcessor:

    def __init__(self, email_info):
        #load secure email information
        try:
            self.email = email_info['address']
            self.password = email_info['password']
            self.mail_server = 'imap.gmail.com' if not 'server' in email_info else email_info['server']
        except Exception as e:
            raise PaymentProcessorException("Could Not Instantiate Payment Processor")

        #connect to the mail server and select inbox
        try:
            self.imap_mail = imaplib.IMAP4_SSL(self.mail_server)
            self.imap_mail.login(self.email, self.password)
            self.imap_mail.list()
            self.imap_mail.select('inbox')
        except Exception as e:
            raise PaymentProcessorException("Could not connect to payment forwarding email.")

        #load running state information for the processor
        try:
            payment_state_filename = "PaymentProcessor_STATE.db"
            with open(payment_state_filename, "rw+") as payment_state_file:
                self.payment_state = yaml.safe_load(payment_state_file)
            if self.email not in self.payment_state:
                self.payment_state[self.email] = {'last_uid' : 0}
            self.last_uid = self.payment_state[self.email]['last_uid']
        except Exception as e:
            raise PaymentProcessorException("Error when loading payment processor State")

    
    def check_for_payments(self):
        new_payments = []
        result, data = self.imap_mail.uid('search', None, "ALL")
        email_uids = data[0].split()
        for x in range(self.last_uid, len(email_uids)):
            new_email_uid = email_uids[x]
            result, email_data = self.imap_mail.uid('fetch', new_email_uid, '(RFC822)')
            raw_email = email_data[0][1]
            raw_email_string = raw_email.decode('utf-8')

            #if this is not a payment we will skip the email
            if "venmo" not in raw_email_string:
                continue

            email_message = email.message_from_string(raw_email_string)
            for part in email_message.walk():
                if part.get_content)type() == "text/html":
                    body = part.get_payload(decode=True)
                    body = str((body.decode('utf-8')))

                    cleanhtml = re.compile("<.*?>")
                    body = re.sub(cleanhtml, '', body)

                    lines = [l.lstrip() for l in body.split('\n')]
                    lines = list(filter(None, lines))
                    
                    #arbitrary check to make sure its not an empty html segment
                    if len(lines > 10):
                        continue

                    relative_index = lines.index('paid\r')
                    payee_line_relative = -1
                    description_line_relative = 4
                    date_amount_line_relative = 8



                    payee = lines[relative_index + payee_line_relative].strip()
                    description_string = lines[relative_index + description_line_relative]
                    amount_string = lines[relative_index + date_amount_line_relative]
                    recieved_date = ' '.join(email_message['Date'].split(' ')[0:-1])

                    date_epoch = datetime.strptime(recieved_date, "%a, %d %b %Y %H:%M:%S").timestamp()
                    dollar_amount = amount_string[amount_string.index('$')+1:date_amount_raw.index('\r')]
                    new_payments.append(Payment(new_email_uid, date_epoch, dollar_amount, description))
                    break