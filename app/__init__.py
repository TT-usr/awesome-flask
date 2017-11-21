from flask import Flask
# 原flask.ext.mongoengine 已过期
from flask_mongoengine import MongoEngine


app = Flask(__name__)

# 在app包中实例化Flask的应用，从config.py中加载配置。
app.config.from_object('config')

# 实例化MongoEngine
db = MongoEngine(app)

from app import views, models