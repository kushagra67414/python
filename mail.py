
import smtplib
import email.utils
import datetime
sender_mail = 'sender@gmail.com'
receivers_mail = ['reciever@gmail.com']
message = """From: From Person %s 
To: To Person %s 
Subject: Sending SMTP e-mail  
This is a test e-mail message. 
"""%(sender_mail,receivers_mail)
try:
   password = input('Enter the password');
   smtpObj = smtplib.SMTP('gmail.com',587)
   smtpobj.login(sender_mail,password)
   smtpObj.sendmail(sender_mail, receivers_mail, message)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")