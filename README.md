Flask Email Trigger App

**Introduction**
This Flask web application sends an email when a specific endpoint is accessed. I use it to initiate a quest for my lovely Nas'ka

**Features**
Flask web server for handling HTTP requests.
Email sending functionality via SMTP.
Configurable through external configuration files for enhanced security.
Ready for manual setup and deployment to cloud platforms like Heroku.

**Prerequisites**
Before you start, ensure you have:

Python 3.6 or higher installed.
An 16-digit app password generated within Gmail account.

**Setup and Installation**

git clone https://github.com/your-username/your-repo-name.git
pip install Flask

**Configure Email Settings:**

Create a config.py file in the root directory with the following content:

SMTP_USERNAME = "your-email@gmail.com"
SMTP_PASSWORD = "your-app-password-from-google-account"

Make sure to replace the placeholder values with your actual email credentials.

**Add config.py to .gitignore**

To keep your credentials secure, ensure config.py is listed in your .gitignore file.

**Running the Application**

python app.py

**Access the App:**

Visit http://127.0.0.1:5000/send_email in a web browser to trigger the email sending function.
