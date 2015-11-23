import smtplib


fromaddr = "YOUR_EMAIL_HERE@gmail.com"
toaddr = "RECIPIENT_EMAIL@gmail.com"

msg = "Hello this is an an automted script, please ignore"

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(fromaddr, "YOUR_PASSWORD_HERE")
server.sendmail(fromaddr, toaddr, msg)
server.quit()