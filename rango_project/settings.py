import os

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django 的安全密钥（请替换为你的密钥）
SECRET_KEY = 'your-secret-key'

# 开发环境开启 DEBUG
DEBUG = True

# 允许的主机
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ✅ 已注册的应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # ✅ 确保 session 应用已启用
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rango',
]

# ✅ 中间件配置
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL 配置
ROOT_URLCONF = 'tango_with_django_project.urls'

# ✅ Django 模板配置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 确保模板目录正确
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI 配置
WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'

# ✅ 数据库配置（默认 SQLite）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# 用户密码验证
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ 国际化设置
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ 静态文件配置
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ✅ 媒体文件配置（用于用户上传的图片）
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ✅ Session 配置（用于访问次数统计）
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # 存储 session 数据到数据库
SESSION_COOKIE_AGE = 1209600  # 2 周（14 天）
SESSION_SAVE_EVERY_REQUEST = True  # 每次请求都更新 session 过期时间

# ✅ 设置默认主键字段类型（兼容 Django 3.2+）
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'