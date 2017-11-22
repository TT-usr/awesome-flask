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

@app.route('/done/<string:todo_id>', methods=['POST',])
def done(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.status = 1
	todo.save()
	todos = Todo.objects.all()
	return render_template('index.html',todos=todos)

@app.route('/undone/<string:todo_id>', methods=['POST',])
def undone(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.status = 0
	todo.save()
	todos = Todo.objects.all()
	return render_template('index.html',todos=todos)

@app.route('/delete/<string:todo_id>')
def delete(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.delete()
	todos = Todo.objects.all()
	return render_template('index.html', todos=todos)







