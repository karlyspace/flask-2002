"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: users.py
@time: 2020/8/24 16:24
"""
import os


from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from apps.models import User
from apps.forms import RegisterForm, LoginForm, UploadForm
from apps.exts import db
from apps.email import send_mail
from flask_login import login_user, logout_user, login_required, current_user
from apps.exts import photos

from PIL import Image

users = Blueprint("users",__name__)


@users.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate():
        u = User.query.filter_by(username=form.username.data).first()
        if not u:
            flash('该用户名不存在')
        elif not u.confirmed:
            flash('该用户还没激活')
        elif u.verify_password(form.password.data):
            login_user(u,remember=form.remember.data)
            flash('登录成功')
            #如果连接中有next 参数 那么我们就跳到这个地址
            #如果没有next 那么就跳转到首页
            # print(request.args['next'])
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('无效的密码')
    return render_template('users/login.html',form=form)

@users.route('/logout/')
def logout_demo():
    logout_user()
    flash('退出登录成功')
    return redirect(url_for('main.index'))

@users.route('/profile/')
@login_required #装饰器必须写在路由的下面
def profile():
    return '个人中心'


@users.route('/test/')
@login_required #装饰器必须写在路由的下面
def test():
    return 'test'

@users.route('/register/',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate():
        u = User(username= form.username.data,password = form.password.data,
        email = form.email.data)
        db.session.add(u)
        db.session.commit()

        #生成一个加密的字符串 保存该用户注册成功后的信息
        token = u.generate_token()
        #发送给用户一封邮件
        send_mail(u.email,'77账户激活','email/activate',username=u.username,token=token)
        return redirect(url_for('users.login'))
    return render_template('users/register.html',form=form)

#当用户点击链接 然后这个方法响应
@users.route('/activate/<token>/')
def activate_user(token):
    if User.check_activate_token(token):
        flash('账户已经激活')
        return redirect(url_for('users.login'))
    else:
        flash('账户激活失败')
        return redirect(url_for('main.index'))

@users.route('/change_icon/',methods=['GET','POST'])
@login_required
def change_icon():
    #current_user 当前登录的用户
    print(current_user.icon)
    form = UploadForm()
    img_url = ''
    if form.validate():
        # 随机文件名
        suffix = os.path.splitext(form.icon.data.filename)[1]
        filename = random_string()+suffix
        photos.save(form.icon.data,name=filename)
        #文件缩略图
        pathname = os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],filename)
        img = Image.open(pathname)
        img.thumbnail((128,128))
        img.save(pathname)

        #获取上传后文件的地址 然后返回到页面上
        # img_url = photos.url(filename)
        #current_user 直接获取当前登录的用户
        if current_user.icon != 'default.jpg': #说明已经上传过一次头像
            os.remove(os.path.join(current_app.config['UPLOADED_PHOTOS_DEST'],current_user.icon))
        current_user.icon = filename
        db.session.commit()
        flash('头像上传完毕')
        return redirect(url_for('users.change_icon'))
    img_url = photos.url(current_user.icon) #从数据库中取出图片的地址 然后展示页面上
    print(img_url)
        #新的地址要保存到数据库中
    return render_template('users/change_icon.html',form=form,img_url=img_url)

def random_string(length=20):
    import random
    base_dir = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(random.choice(base_dir) for i in range(length))

