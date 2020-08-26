"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: manage.py
@time: 2020/8/24 16:20
"""
import time

from flask_script import Manager
from apps import create_app
from flask_migrate import MigrateCommand

from apps.exts import db
from apps.models import User,Posts

app = create_app('default')
manager = Manager(app)
manager.add_command('db',MigrateCommand)

@manager.command
def create_test_post():
    # 内容  作者
    for x in range(1,200):
        content = '内容:%s' % x
        author = User.query.first()
        post = Posts(content=content,author=author)
        time.sleep(0.2)
        db.session.add(post)
        db.session.commit()
    print('帖子添加成功')

if __name__ == '__main__':
    manager.run()

