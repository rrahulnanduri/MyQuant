import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_signal_email(receiver_email, subject, message):
    global server
    sender_email = "your_email@example.com"
    password = "your_password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email sent successfully!')
    except Exception as e:
        print('Email could not be sent:', str(e))
    finally:
        server.quit()
