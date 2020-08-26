"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: posts.py
@time: 2020/8/26 14:21
"""
from apps.exts import db
from datetime import datetime


# id  rid
# 1     0
# 2     0
# 3     0
# 4     1
# 5     1
# 6     1

# 查看文章的详情 id
# 帖子
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    rid = db.Column(db.Integer,index=True,default=0)
    content = db.Column(db.Text)
    pub_time = db.Column(db.DateTime,default=datetime.utcnow)

    uid = db.Column(db.Integer,db.ForeignKey('users.id'))
    author = db.relationship('User',backref = 'postes')


