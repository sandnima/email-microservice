import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


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
        with smtplib.SMTP_SSL(os.getenv('HOST'), int(os.getenv('PORT'))) as server:
            server.ehlo()
            server.login(os.getenv('GMAIL_USERNAME'), os.getenv('GMAIL_PASSWORD'))
            server.sendmail(sent_from, to, message.as_string())
    except Exception as e:
        print('Something went wrong...\n%s'.format(e))


if __name__ == '__main__':
    sent_from = 'Our Team'
    to = ['test@gmail.com']
    subject = 'OMG Super Important Message'
    body = "Here is a simple test"
    send_email(sent_from=sent_from, to=to, subject=subject, body=body)
