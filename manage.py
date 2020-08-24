"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: manage.py
@time: 2020/8/24 16:20
"""
from flask_script import Manager
from apps import create_app

app = create_app('product')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()

