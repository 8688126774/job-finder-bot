import smtplib
from email.mime.text import MIMEText

sender = "your_email@gmail.com"
password = "your_password"
receiver = "your_email@gmail.com"

message = MIMEText("New job listings are available. Check the CSV file.")

message["Subject"] = "Daily Job Alert"
message["From"] = sender
message["To"] = receiver

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
server.sendmail(sender, receiver, message.as_string())

server.quit()

print("Email sent successfully")
