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
 				 		
# 书中写的是 flask.ext.wtf import From 已经改为:
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# WTForms支持的HTML标准字段

# StringField 文本字段
# TextAreaField 多行文本字段
# PasswordField 密码文本字段
# HiddenField 隐藏文本字段
# DateField 文本字段，值为 datetime.date 格式
# DateTimeField 文本字段，值为 datetime.datetime 格式
# IntegerField 文本字段，值为整数
# DecimalField 文本字段，值为 decimal.Decimal
# FloatField 文本字段，值为浮点数
# BooleanField 复选框，值为 True 和 False
# RadioField 一组单选框
# SelectField 下拉列表
# SelectMultipleField 下拉列表，可选择多个值
# FileField 文件上传字段
# SubmitField 表单提交按钮
# FormField 把表单作为字段嵌入另一个表单
# FieldList 一组指定类型的字段


# WTForms验证函数

# Email 验证电子邮件地址
# EqualTo 比较两个字段的值；常用于要求输入两次密码进行确认的情况
# IPAddress 验证 IPv4 网络地址
# Length 验证输入字符串的长度
# NumberRange 验证输入的值在数字范围内
# Optional 无输入值时跳过其他验证函数
# Required 确保字段中有数据
# Regexp 使用正则表达式验证输入值
# URL 验证 URL
# AnyOf 确保输入值在可选值列表中
# NoneOf 确保输入值不在可选值列表中


class NameForm(Form):
	# StringField 类表示属性为 type="text" 的 <input> 元素
	# StringField 构造函数中的可选参数 validators 指定一个由验证函数组成的列表，在接受用户提交的数据之前验证数据
	# 验证函数 Required() 确保提交的字段不为空
	name = StringField('what is your name', validators=[Required()])
	# SubmitField 类表示属性为 type="submit" 的 <input> 元素
	submit = SubmitField('submit')
		
