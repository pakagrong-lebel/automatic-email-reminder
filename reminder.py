# Python script to send automatic email reminders
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
def send_reminder_email(sender_email, sender_password, recipient_email, subject, body, reminder_date):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    now = datetime.now()
    reminder_date = datetime.strptime(reminder_date, '%Y-%m-%d')
    if now.date() == reminder_date.date():
        message = MIMEText(body, 'plain')
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        server.sendmail(sender_email, recipient_email, message.as_string())
        server.quit()