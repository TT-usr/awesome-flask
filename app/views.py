# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from app.models import Todo
# 这个包还得导入,日了蛋
from flask import request

@app.route('/')
def index():
	todos = Todo.objects.all()
	return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST',])
def add():
	content = request.form.get("content")
	todo = Todo(content=content)
	todo.save()
	todos = Todo.objects.all()
	return render_template('index.html', todos=todos)