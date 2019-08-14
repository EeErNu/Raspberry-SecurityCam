import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage

def sendEmail(snapshot):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    msg = MIMEMultipart()
    msg["Subject"] = "Security Camera"
    msg.attach(MIMEImage(file(snapshot).read()))

    server.login("email@gmail.com", "pswd")
    server.sendmail("max.kurylovych@gmail.com", "max.kurylovych@gmail.com", msg.as_string())