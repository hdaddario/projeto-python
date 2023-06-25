import os
import smtplib
from email.message import EmailMessage

login = 'ddxfire2@gmail.com'
senha = 'daddariox1234'

msg = EmailMessage()
msg['Subject'] = 'teste de email'
msg['From'] = login
msg['To'] = login
msg.set_content= 'teste de email'

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(login,senha)
s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
