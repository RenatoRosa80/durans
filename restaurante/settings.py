from pathlib import Path    
import os

BASE_DIR = Path(__file__).resolve().parent.parent   

# Configuração de arquivos estáticos
STATIC_URL = '/static/'  # <- essa linha é obrigatória
STATIC_ROOT = BASE_DIR / 'staticfiles'  # usado no Render (produção)

# Caminho para os arquivos estáticos durante o desenvolvimento
STATICFILES_DIRS = [
    BASE_DIR / 'reserva' / 'static',  # substitua 'restaurante' pelo nome do SEU app
]

# Configuração de mídia (caso use upload de imagens)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Segurança para produção
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'projeto-final-6wom.onrender.com']
CSRF_TRUSTED_ORIGINS = ['https://projeto-final-6wom.onrender.com']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4af+)@m6iw3mnx+hs6^^(7a-&_pw8skq#afp5hz&qivu*%od&-'   

# Application definition    
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reserva',
    # Outros aplicativos
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # Outros Middleware de cache

]

ROOT_URLCONF = 'restaurante.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{   
                'staticfiles': 'django.templatetags.static',
                'static': 'django.templatetags.static', 
            }
        },
    },
]

WSGI_APPLICATION = 'restaurante.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True   

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
DATE_INPUT_FORMATS = ['%d/%m/%Y']

# Adiciona o diretório 'static' na raiz do projeto como local de busca
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static') 
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOGIN_REDIRECT_URL = '/reservas/'  # ou qualquer URL que queira
LOGOUT_REDIRECT_URL = '/'  # ou qualquer URL que queira

# settings.py
LOGIN_URL = '/login/'

