import os
import smtplib
import imghdr
from email.message import EmailMessage
os.chdir('C:\\Users\\rajee\\Documents\\Python Scripts')
email_address = 'rajeevkumarsinghji@gmail.com'
email_password = "krishna18"
contacts = ['rajeevkumarsinghji@gmail.com','rajeev_singh717@yahoo.com']

msg = EmailMessage()
msg['Subject'] = "check out my picture"
msg['From'] =email_address
msg['to'] = contacts
msg.set_content('Image Attached')

###### Send Images
files = ['raj.jpeg','raj1.jpg']

for file in files:
    with open(file , 'rb') as f:
        file_data =f.read()
        file_type=imghdr.what(f.name)
        file_name = f.name
    
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name)

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_address,email_password)
    smtp.send_message(msg)
    
    
####### Send Pdf files
#files = ['Rajeev Singh.pdf']
#for file in files:
#    with open(file , 'rb') as f:
#        file_data =f.read()
#        file_name = f.name
#        
#    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename = file_name)
#        
#with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#    smtp.ehlo()
#    smtp.starttls()
#    smtp.ehlo()
#    smtp.login(email_address,email_password)
#    smtp.send_message(msg)