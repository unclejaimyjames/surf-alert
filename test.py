
import urllib2
import json
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
msg['Subject'] = "Pi test"

body = "E-mail succesfully sent\nUpdate v1.0\n"

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, text)
server.quit()

