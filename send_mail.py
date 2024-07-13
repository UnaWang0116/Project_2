import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg = MIMEMultipart()
#用dictionary去設定
msg["From"] = "fantasticseven1204@gmail.com"
msg["To"] = "kiol726a@gmail.com"
header = Header("Test Send Email","utf-8")
msg["Subject"] = header.encode() #做編碼

body = "Love you bear this is email send from 寶"
msg.attach(MIMEText(body)) 
#mbody = MIMEText(body) 上面一行等於兩行
#msg.attach(mbody)
ssl._create_default_https_context = ssl._create_unverified_context
ssl_context = ssl.create_default_context()
# google專用的port:465
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
    server.login("fantasticseven1204@gmail.com","vwof aizu vmxn edjg")
    server.sendmail("fantasticseven1204@gmail.com","kiol726a@gmail.com",msg.as_string())
print("success send email")