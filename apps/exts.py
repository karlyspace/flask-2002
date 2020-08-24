"""
@desc: 
@author: 宋慧娟
@contact: QQ:462550768
@file: exts.py
@time: 2020/8/24 16:17
"""
#导入类库

from flask_bootstrap import Bootstrap



#实例化对象

bootstrap = Bootstrap()


#封装函数 完成初始化

def config_extensions(app):
    bootstrap.init_app(app)