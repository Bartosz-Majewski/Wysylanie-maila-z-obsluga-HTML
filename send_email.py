import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from http import server
from os import getenv
from dotenv import load_dotenv
import ssl

load_dotenv()


class GmailAdapter:
    def __init__(self, sender, password):
        self.sender = sender
        self.password = password
        self.smptp_server = getenv('SMTP_SERVER')
        self.port = getenv('PORT')
        # self.context = ssl.create_default_context()
        self.server = smtplib.SMTP_SSL(
            self.smptp_server, self.port)

    def login(self):
        self.server.ehlo()
        self.server.login(self.sender, self.password)

    def _compose_message(self, reveiver_email, subject, body_message):
        message = MIMEMultipart('alternative')
        message['From'] = self.sender
        message['To'] = reveiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body_message, 'html'))

        return message

    def sendmail(self, receiver_email, subject, body_message):
        message = self._compose_message(receiver_email, subject, body_message)
        self.server.sendmail(self.sender, receiver_email, message.as_string())

    def __del__(self):
        self.server.close()
