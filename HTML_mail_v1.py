import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "my@email.com"
you = "your@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you


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
