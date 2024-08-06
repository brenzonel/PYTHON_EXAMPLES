import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv(override=True)

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = os.getenv('USER')
    msg['from'] = user
    pwd = os.getenv('PWDAPP')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, pwd)
    server.send_message(msg)

    server.quit()

if __name__ == '__main__':
    email_alert('Alerta', 'Esto es una alerta', 'correo@correo.com')
                