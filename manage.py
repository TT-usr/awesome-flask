# -*- coding: utf-8 -*-

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver",
         Server(host='0.0.0.0',port=5001, use_debugger=True))

if __name__ == '__main__':
    manager.run()