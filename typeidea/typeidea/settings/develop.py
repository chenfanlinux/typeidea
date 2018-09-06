from .base import *  # NOQA
DEBUG = True
ALLOWED_HOSTS = ['*']

# INSTALLED_APPS += (
#     'debug_toolbar',  # 调试项目的性能
# )


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'blog',
    'config',
    'comment',
    'typeidea',
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'chenfanlinux1',  # 数据库的名字
#         'USER': 'root',  # 连接数据库的用户名
#         'PASSWORD': '123456',  # 用户对应的密码
#         'HOST': 'localhost',  # 指定mysql数据库所在电脑的ip
#         'PORT': 3306,  # mysql服务的端口号
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

