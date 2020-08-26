"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: posts.py
@time: 2020/8/26 14:33
"""
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length


#用户注册表单
class PostsForm(FlaskForm):
    content = TextAreaField('',render_kw={'placeholder':'这一刻想留下点什么话...'},validators=[DataRequired(),Length(min=10,max=144,message='至少需要写10个字')])
    submit = SubmitField('即刻发表')

