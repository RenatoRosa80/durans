from pathlib import Path    
import os

BASE_DIR = Path(__file__).resolve().parent.parent   

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4af+)@m6iw3mnx+hs6^^(7a-&_pw8skq#afp5hz&qivu*%od&-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False  # Alterado para False em produção

ALLOWED_HOSTS = [
    'durans.onrender.com',
    'localhost',
    '127.0.0.1',
    '.onrender.com',  # Adicionado para todos os subdomínios do Render
]

CSRF_TRUSTED_ORIGINS = [
    'https://durans.onrender.com',
    'https://*.onrender.com',
]

# Application definition    
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reserva',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ADICIONADO - deve vir logo após SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # REMOVIDO: 'django.middleware.security.SecurityMiddleware' duplicado
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

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Formatos de data
DATE_INPUT_FORMATS = ['%d/%m/%Y']

# Configuração de arquivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Caminho para os arquivos estáticos durante o desenvolvimento
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'reserva/static'),  # Mantenha APENAS esta configuração
]

# Configuração do WhiteNoise para arquivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuração de mídia (caso use upload de imagens)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configurações de login/logout
LOGIN_REDIRECT_URL = '/reservas/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

# Para desenvolvimento local, você pode usar esta verificação
if os.environ.get('DEBUG', '').lower() == 'true':
    DEBUG = True
elif 'RENDER' in os.environ:
    DEBUG = False
else:
    DEBUG = True  # Padrão para desenvolvimento local