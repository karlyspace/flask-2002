# flask-2002
2002flask项目



##目录结构
apps #python包
    __init__.py #项目实例文件
    exts.py   #存放所有的扩展
    config.py #存放项目的配置 配置数据库 配置上传文件
    email.py  #多个地方可能都用到邮件单独拿出来写
    models    #python包 模型要放一起
    forms     #python包 表单要放一起
    views     #python包 存放蓝本文件的目录
    templates #存放页面文件
    static    #存放静态文件
        css
        js
        images
        favicon.ico
manage.py #项目的入口