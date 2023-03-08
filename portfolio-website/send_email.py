import smtplib, ssl, os


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    receiver = "receiver@gmail.com"
    username = "sender@gmail.com"
    password = os.getenv("Password")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
