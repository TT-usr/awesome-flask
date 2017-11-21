from flask import Flask

app = Flask(__name__)

# 在app包中实例化Flask的应用，从config.py中加载配置。
app.config.from_object('config')

from app import views, models