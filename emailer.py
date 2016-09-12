import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 

name = raw_input("Please enter your name: ")
home = raw_input("Where are you from: ")
food = raw_input("What is your favorite food: ")



fromaddr = "krl.wang@gmail.com"
toaddr = "krl.wang@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"




 
body = "Hello %s, you are from %s, and you love to eat %s" %(name, home, food)
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "****")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()