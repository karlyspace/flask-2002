"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: posts.py
@time: 2020/8/24 16:24
"""
from flask import Blueprint,render_template

posts =  Blueprint('posts',__name__)

@posts.route('/posts/')
def index():
    # return render_template('users/posts.html')
    return '您的收藏是我坚持的最大动力，谢谢！！'