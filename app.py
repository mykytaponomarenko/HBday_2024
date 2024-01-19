from flask import Flask
import smtplib
from email.mime.text import MIMEText
import config  # Імпорт конфігураційного файлу

app = Flask(__name__)

# Функція для відправлення електронної пошти
def send_email(recipient, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = config.SMTP_USERNAME
    msg['To'] = recipient

    # Підключення до SMTP сервера та відправлення листа
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
    server.sendmail(config.SMTP_USERNAME, recipient, msg.as_string())
    server.quit()

# Перевірка запуску Flask app
@app.route('/')
def home():
    return "Flask is running!"

# Активації відправлення листа
@app.route('/send_email')
def trigger_email():
    send_email('drponchek@ukr.net', 'Test Email', 'Це тестовий лист від Flask.')
    return "Лист відправлено!"

if __name__ == '__main__':
    app.run(debug=True)
