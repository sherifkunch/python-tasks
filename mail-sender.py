import smtplib

from_address = "...@gmail.com"
to_address = "...@gmail.com"

msg={}

msg['From'] = from_address
msg['To'] = to_address

print(type(msg))
print(msg)

# Create the message .
text = """\
Sending an email using Python and Gmail, how fun!
"""


# Credentials
username = ''  
password = ''

#Sending the email
# note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.ehlo()
server.starttls()
server.login(username,password)  
server.sendmail(from_address, to_address, "Subject: Test email\n\n"+text)  
server.quit()