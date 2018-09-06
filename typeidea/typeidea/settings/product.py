from .base import *  # NOQA
DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'chenfanlinux1',  # 数据库的名字
        'USER': 'root',  # 连接数据库的用户名
        'PASSWORD': '123456',  # 用户对应的密码
        'HOST': 'localhost',  # 指定mysql数据库所在电脑的ip
        'PORT': 3306,  # mysql服务的端口号
    }
}
