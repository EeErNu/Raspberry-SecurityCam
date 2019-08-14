import smtplib

# def sendEmail(msg):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#
#     server.login("max.kurylovych@gmail.com", "yoberber123")
#     server.sendmail("max.kurylovych@gmail.com", "max.kurylovych@gmail.com", msg)

# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEImage import MIMEImage
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
#
# server.ehlo()
# server.starttls()
# server.ehlo()
#
# msg = MIMEMultipart()
# msg.attach(MIMEImage(file("test_image.png").read()))
#
# server.login("max.kurylovych@gmail.com", "yoberber123")
# server.sendmail("max.kurylovych@gmail.com", "max.kurylovych@gmail.com", msg.as_string())

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

    server.login("max.kurylovych@gmail.com", "yoberber123")
    server.sendmail("max.kurylovych@gmail.com", "max.kurylovych@gmail.com", msg.as_string())