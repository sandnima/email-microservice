import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

# env variables
HOSTNAME = os.getenv('HOST')
PORT = int(os.getenv('PORT'))
GMAIL_USERNAME = os.getenv('GMAIL_USERNAME')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')


def send_email(sent_from: str = None, to: list = None, subject: str = None, body: str = None):
    assert sent_from
    assert to
    assert subject
    assert body

    message = EmailMessage()
    message["From"] = sent_from
    message["To"] = ", ".join(to)
    message["Subject"] = subject
    message.set_content(body)

    try:
        with smtplib.SMTP_SSL(HOSTNAME, PORT) as server:
            server.ehlo()
            server.login(GMAIL_USERNAME, GMAIL_PASSWORD)
            server.sendmail(sent_from, to, message.as_string())
    except Exception as e:
        print('Something went wrong...\n%s'.format(e))
