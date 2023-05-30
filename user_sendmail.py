import smtplib


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('abimbola086@gmail.com', '09021238570')
    server.sendmail('abimbola086@gmail.com', to, content)
    server.close()