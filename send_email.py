import smtplib
 
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
 
sender = 'jthebutler@gmail.com'
password = 'jeevesisguessable'
recipient = 'bc389@cam.ac.uk'
subject = 'The CousCous Roundup'
body = 'There is couscous coming on Saturday. Shit the bed.'
 
"Sends an e-mail to the specified recipient."
 
body = "" + body + ""
 
headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)
 
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
 
session.ehlo()
session.starttls()
session.ehlo
session.login(sender, password)
 
session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()