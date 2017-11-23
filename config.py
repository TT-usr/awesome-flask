import os

MONGODB_SETTINGS = {'DB': 'todo_db'}
# 为了实现 CSRF 保护，Flask-WTF 需要程序设置一个密钥
SECRET_KEY = 'cgpjugxZyGxqApiCvELjxETHfbrGZEeGdDNyKvueBpMFtB4dTYUZgEKsPhrazRfr'

MAIL_SERVER = 'smtp.googlemail.com'

MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')