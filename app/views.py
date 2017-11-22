# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from app.models import Todo, TodoForm
# 这个包还得导入,日了蛋
from flask import request, current_app, make_response, redirect, abort
# 导入 bootstrap
from flask_bootstrap import Bootstrap
# 导入 Moment( 格式化时间 )
from flask_moment import Moment
from datetime import datetime

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/time')
def time():
	return render_template('user.html', current_time = datetime.utcnow())


# 动态路由
@app.route('/user/<name>')
def user(name):
	# 打印请求头
	# print(request.headers)

	# 程序上下文
	# print(current_app.name)

	# 程序所有的路由
	# print(app.url_map)
	
	# return '<h1>hello, %s</h1>' % name

	# 第二个参数是 http 状态码
	# return '我是404哦', 404

	# 还可以返回 response
	# response = make_response('<h1>hello, %s</h1>' % name)
	# response.set_cookie('key','value')
	# return response

	# 重定向
	# return redirect('http://www.baidu.com')

	# abort 不会把控制权交还给调用它的函数，而是抛出异常把控制权交给 Web 服务器
	# abort(404)

	return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500


@app.route('/')
def index():
	form = TodoForm()
	todos = Todo.objects.all()
	return render_template('index.html', todos=todos, form=form)

@app.route('/add', methods=['POST',])
def add():
	form = TodoForm(request.form)
	if form.validate_on_submit():
		content = request.form.get("content")
		todo = Todo(content=content)
		todo.save()
	todos = Todo.objects.all()
	return render_template('index.html', todos=todos, form=form)

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







