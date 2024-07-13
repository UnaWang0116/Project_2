import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

alot_reciver = ["kiol726a@gmail.com","han998775@gmail.com"]

for reciver in alot_reciver:
    msg = MIMEMultipart()
    #用dictionary去設定
    sender = "fantasticseven1204@gmail.com"
    msg["From"] = sender
    msg["To"] = reciver
    header = Header("Tomorrow dating","utf-8")
    msg["Subject"] = header.encode() #做編碼

    body = "I want to have a good date tomorrow loveyou Frank"
    msg.attach(MIMEText(body)) 
    #mbody = MIMEText(body) 上面一行等於兩行
    #msg.attach(mbody)
    #ssl._create_default_https_context = ssl._create_unverified_context
    ssl_context = ssl.create_default_context()
    # google專用的port:465
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login(sender,"vwof aizu vmxn edjg")
        server.sendmail(sender,reciver,msg.as_string())

    print("success send email")