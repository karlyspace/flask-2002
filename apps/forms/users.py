"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: users.py
@time: 2020/8/25 11:19
"""
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo
from wtforms.validators import ValidationError
from flask_wtf.file import FileField,FileRequired,FileAllowed
from apps.models import User
from apps.exts import photos

#用户注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(6,20,message="用户名在6到20位之间")])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,30,message='密码必须在6到30位之间')])
    confirm = PasswordField('确认密码',validators=[EqualTo('password',message='两次密码必须一致')])
    email = StringField('邮箱',validators=[Email(message='邮箱格式不正确')])
    submit = SubmitField('立即注册')

    #用户名 和 邮箱 这两个  光符合上面的要求还不够 收到用户提交后
    #从数据库进行查询判断是否已经存在

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户名已经存在,请更换其它用户名')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱名已经存在,请更换其它邮箱名')

#用户登录表单
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(6, 20, message="用户名在6到20位之间")])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 30, message='密码必须在6到30位之间')])
    remember = BooleanField('记住我')
    submit = SubmitField('立即登录')

# 用户上传文件表单
class UploadForm(FlaskForm):
    icon = FileField('头像',validators=[FileRequired('请选择头像'),FileAllowed(photos,message='只能上传图片')])
    submit = SubmitField('点击上传')

