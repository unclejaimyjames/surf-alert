
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "surfmelding@gmail.com"
toaddrs  = ['jaimyvanderheijden@gmail.com']

username = "surfmelding@gmail.com"
password = "surfsurfsurf"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddrs)
msg['Subject'] = "HTML test"

html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/">link</a> you wanted.
    </p>
  </body>
</html>
"""

part1 = MIMEText(html, 'html')
msg.attach(part1)

print msg.as_string()

