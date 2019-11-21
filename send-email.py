import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_content = "Usted tiene un turno con el medico XXXXXX en la fecha Febrero-1 a las 10 am"

#The mail addresses and password
sender_address = 'utnprogramacion3@gmail.com'
sender_pass = 'h51kolv3'
receiver_address = 'msarfernandez@docentes.frgp.utn.edu.ar'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Hospital Super Cosmico'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
