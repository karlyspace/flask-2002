"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: users.py
@time: 2020/8/25 10:13
"""
from flask import current_app
from apps.exts import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32),unique=True)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(64),unique=True)
    #是否激活
    confirmed = db.Column(db.Boolean,default=False)
    icon = db.Column(db.String(128),default='default.jpg')

    @property #把方法可以当成属性来调用
    def password(self):
        raise AttributeError('密码不可读属性')

# password 对外
#对内  password_hash  加密后
#密码永不返回
#密码不可读
    #password表示的是用户传递过来的密码
    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    #密码校验  参数为用户提交的密码
    # 先对用户的提交的密码 进行加密 然后跟数据库中存在的加密的密码进行比较
    #正确返回True 否则返回False
    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    #生成token的方法 设置过期时间
    def generate_token(self,expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expires_in=expires_in)
        return s.dumps({'id':self.id}) #把用户的id 藏到加密的字符串中


    #服务器收到以后 解密 然后拿出id 然后就知道 是哪个用户要激活
    @staticmethod
    def check_activate_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = s.loads(token) #解密 之前加密的字符串
        except:
            return False
        u = User.query.get(data.get('id'))  #解密后拿到 藏的用户id
        #根据这个id 取出用户的详细信息
        if not u:
            return False
        if not u.confirmed:
            u.confirmed = True
            db.session.commit()
        return True

#登录认证的回调
#登录成功以后存的是用的id
#需要一个方法根据用户的id 取出用户的详细信息
@login_manager.user_loader
def load_user(uid):
    return User.query.get(uid)