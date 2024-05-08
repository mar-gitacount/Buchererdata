import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 送信元と宛先のメールアドレス
sender_email = "masaru.work.contact@gmail.com"
receiver_email = "ichikawa.contact@gmail.com"

# メールサーバーの設定
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "masaru.work.contact@gmail.com"
smtp_password = "masaruwork"

# メール内容の作成
subject = "Test Subject"
body = "This is a test email from Python."

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))

# SMTPサーバーへの接続とメール送信
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully.")
