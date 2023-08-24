from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

class EmailSender:
    def __init__(self, email_address, password, to_address):
        self.email_address = "vikramathithyan99@gmail.com"
        self.password = "jguinpzxcwsksieu"

    def send_mail(self, filename, attachment, toaddr, key):
        fromaddr = self.email_address

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Log File"

        body = key
        msg.attach(MIMEText(body, 'plain'))

        attachment_file = open(attachment, 'rb')
        attachment_payload = attachment_file.read()
        attachment_file.close()

        attachment_part = MIMEBase('application', 'octet-stream')
        attachment_part.set_payload(attachment_payload)
        encoders.encode_base64(attachment_part)
        attachment_part.add_header('Content-Disposition', f"attachment; filename = {filename}")
        msg.attach(attachment_part)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, self.password)

        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)

        s.quit()