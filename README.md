# awesome-flask

###运行环境要求
`MongoDB`
安装可以使用 HomeBrew 一键安装
`brew install mongodb`
启动本地 MongoDB 服务
`mongod`


创建虚拟环境
1.安装虚拟环境
`python3 install virtualenv`
2.创建虚拟环境(在本工程目录内)
`virtualenv env`
3.激活虚拟环境
`source env/bin/activate`

`locale.Error: unsupported locale setting` *这个错误会出现在云端 Linux 上,解决办法为执行`export LC_ALL=C`*

###安装依赖
`pip install -r requirenments.txt`

###运行项目
`python manage.py runserver`

```
optional arguments:

 -h, --help 
 
 -t HOST, --host HOST
 
 -p PORT, --port PORT
 
 --threaded
 
 --processes PROCESSES
 
 --passthrough-errors
 
 -d, --no-debug
 
 -r, --no-reload
 
```

