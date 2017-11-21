# -*- coding: utf-8 -*-

# 原 flask.ext.script 已过期
from flask_script import Manager, Server
from app import app
from app.models import Todo

manager = Manager(app)

manager.add_command("runserver",
         Server(host='0.0.0.0',port=5001, use_debugger=True))


@manager.command
def save_todo():
	todo = Todo(content='my first todo')
	todo.save()

if __name__ == '__main__':
    manager.run()