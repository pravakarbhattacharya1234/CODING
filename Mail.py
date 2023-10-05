 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "youraddress@gmail.com"
toaddr = "some other email address"
msg = MIMEMultipart()
'''Multipurpose Internet Mail Extensions (MIME) is an Internet standard 
that extends the format of email to support'''
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Subject"
body = "Write your message here"
msg.attach(MIMEText(body, 'plain'))
#create a SMTP object which is going to be used for connection with the server.
server = smtplib.SMTP('smtp.gmail.com:587')
'''STARTTLS is a way to take an existing insecure connection and upgrade it 
to a secure connection using SSL/TLS. '''
server.starttls()
server.login(fromaddr, "your password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
'''SMTPAuthenticationError when sending mail using gmail
Go to this link and select Turn On
https://www.google.com/settings/security/lesssecureapps
Moreover google block an ip when you try to send a email since a unusual location, so, you can unblock in the next link
https://support.google.com/accounts/answer/6009563
and clicked in
accounts.google.com/DisplayUnlockCaptcha .'''