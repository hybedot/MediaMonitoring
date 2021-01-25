import os
from typing import List
import smtplib

#this will be moved to app.py module
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)

EMAIL = os.environ.get("EMAIL", None)
PASSWORD = os.environ.get("PASSWORD", None)
SMTP = os.environ.get("SMTP", None)
SMTP_PORT = os.environ.get("SMTP_PORT", None)

FAILED_LOAD_EMAIL = 'Failed to load email'
FAILED_LOAD_PASSWORD = 'Failed to load password'
FAILED_LOAD_SMTP = 'Failed to load SMTP'
FAILED_LOAD_SMTP_PORT = 'Failed to load SMTP port'



# getTwit function
# connect to twitter
# check if connection exits and log info:
# get tweets
# log error if connection does not exits



# database  connection function




# Send mail fucntion
# send mail when result of the prdiction is complete
# input to the fucntion will be the list of the recipients(main and copy recipients)
# use loguru to log message instead of print
# write a function to get the list of mail recipients

class MailerException(Exception):
    def __init__(self, message):
        super().__init__(message)

def getEmailBody():
    return 'hello'

def getEmailSubject():
    return 'hello'


def sendMail(sender, email):
        subject = getEmailSubject()
        body = getEmailBody()
        
        if EMAIL is None:
            raise MailerException(FAILED_LOAD_EMAIL)

        if PASSWORD is None:
            raise MailerException(FAILED_LOAD_PASSWORD)
        
        if SMTP is None:
            raise MailerException(FAILED_LOAD_SMTP)
        
        if SMTP_PORT is None:
            raise MailerException(FAILED_LOAD_SMTP_PORT)
        
        try:
            server = smtplib.SMTP(SMTP, SMTP_PORT)
            server.ehlo()
            server.starttls()
            server.ehlo()
            
            try:
                server.login(EMAIL, PASSWORD)

                msg = f'Subject: {subject}\n\n{body}'
                
                server.sendmail(
                    sender,
                    email,
                    msg
                )
                print ('Email sent')
            finally:
                server.quit()

        except smtplib.SMTPAuthenticationError:
            print ('Error: Your email or password is incorrect')
        except smtplib.SMTPException as e:
            print(e)



