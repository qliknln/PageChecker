import smtplib
from email.mime.text import MIMEText


class MyMail(object):
    def __init__(self):
        pass

    @staticmethod
    def send_mail(subject, text, recipient):
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = 'PageChecker@qlik.com'
        msg['To'] = recipient
        s = smtplib.SMTP('smtp.qliktech.com')
        s.send_message(msg)
        s.quit()