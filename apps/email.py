"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: email.py
@time: 2020/8/24 16:17
"""
from threading import Thread
from flask import render_template,current_app
from apps.exts import mail
from flask_mail import Message


# 异步发送邮件
def async_send_mail(app,msg):
    # 发送邮件需要程序上下文，新的线程没有上下文，需要手动创建
    with app.app_context():
        mail.send(message=msg)

# 封装函数，实现邮件发送
def send_mail(to,subject,template,**kwargs):
    # 根据current_app获取当前的实例
    app = current_app._get_current_object()
    # 创建message对象
    msg = Message(subject=subject,recipients=[to],sender=app.config['MAIL_USERNAME'])

    # 浏览器打开
    msg.html = render_template(template+".html",**kwargs)
    # 客户端打开
    msg.body = render_template(template+".txt",**kwargs)

    # 创建线程
    thr = Thread(target=async_send_mail,args=(app,msg))
    # 启动线程
    thr.start()

    return thr
