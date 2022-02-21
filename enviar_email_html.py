# Script para envio de email com código html
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SENDER = " "
PASSWORD = " "
RECIPIENT = " "

html = """
<html>
  <head></head>
  <body>
    <h3>Olá!!</h3>
    <p>Como vai?<br>
       Aqui uma página legal pra você! <a href="https://github.com/MayconCampos">link</a>.
    </p>
  </body>
</html>
"""

msg = MIMEMultipart()
msg["Subject"] = "Algum código HTML"
msg["From"] = SENDER
msg["To"] = RECIPIENT
msg.attach(MIMEText(html, "html"))

with smtplib.SMTP("smtp server vai aqui") as connection:
    connection.starttls()
    connection.login(user=SENDER, password=PASSWORD)
    connection.sendmail(from_addr=SENDER, to_addrs=RECIPIENT, msg=msg.as_string())
