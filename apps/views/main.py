"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: main.py
@time: 2020/8/24 16:24
"""
from flask import Blueprint,render_template

main = Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('main/index.html')

