import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class email_sender:

    def __init__(self, domain, port, login, pwd):
        """
        Pass it the SMTP domain and SMTP port
        """
        self.domain = domain
        self.port = port
        self.login = login
        self.pwd = pwd

    def send(self, sender, receiver, subject, body, css=None):
        """
        Send email
        ------ Parameters:
        sender: sender
        receiver: receiver
        subject: email subject
        body: your HTML body
        css: optional. CSS style sheet. Example:
                h1 {
                    font-weight: bold;
                    color: #111
                }
        """

        # create msg container
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = receiver

        html = """<head><style>{0}</style>
                </head><body>{1}</body>""".format(css,body)

        part = MIMEText(html, 'html')
        msg.attach(part)

        server = smtplib.SMTP(self.domain, self.port)
        server.connect(self.domain,self.port)
        # ehlo method is required to authenticate
        server.ehlo()
        # starttls is mandatory to work with gmail SMTP, either SSL/TLS
        server.starttls()
        server.login(self.login,self.pwd)
        server.sendmail(sender,receiver,msg.as_string())
        server.quit()
