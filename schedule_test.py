
import schedule
import time
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
msg['Subject'] = "schedule test"

body = "E-mail succesfully sent\nUpdate v1.1\n"

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

def job():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, text)
    server.quit()

schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

