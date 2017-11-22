# -*- coding: utf-8 -*-

from app import db
import datetime
from flask_mongoengine.wtf import model_form


class Todo(db.Document):
 	content = db.StringField(required=True, max_length=20)
 	time = db.DateTimeField(default=datetime.datetime.now())
 	status = db.IntField(default=0)

# 通过Todo类生成TodoForm类, 数据库中的验证条件就和表单验证条件达成一致。
TodoForm = model_form(Todo)
 				 		