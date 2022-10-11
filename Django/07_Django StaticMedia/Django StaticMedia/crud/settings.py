"""
Django settings for crud project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'articles',
    'accounts',
    'django_extensions',
    'imagekit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'crud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_ROOT = BASE_DIR / 'staticfiles' # 경로는 원하는 곳에 두면 됨. BASE 디렉토리에 'staticfiles' 폴더에 두겠다
# cf) collectstatic : STATIC_ROOT에 장고 프로젝트의 모든 정적 파일을 수집
#   python manage.py collectstatic # collectstatic이 저 경로에 장고에 내장되어 있던 모든 정적파일을 다 뱉을 것
#   133 static files copied, staticfiles 폴더에
#   admin 페이지에 폰트나 이미지 등 자동으로 구성되어 있잖아
#   배포했을 때 다른 컴퓨터를 위해서

# 추가 경로 작성
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# BASE에 static 폴더 생성
# BASE_DIR / 'crud/static', 로 바꾸면 crud 폴더 내 static 폴더에 이미지 저장 후 index.html에서 부르면 해당 이미지가 출력됨(이미지파일 영문으로 해야 개발자도구에서 주소 명확히 확인 가능)

STATIC_URL = '/static/'
# 기본값 : None이지만 ‘/static/’로 덮어씌여짐 
# STATIC_ROOT(내장된 정적파일의 실제 절대경로)에 있는 정적 파일을 참조할 때 사용할 URL (URL을 만드는 주소값이 STATIC_URL)
# 개발단계에서는 실제 정적파일들이 저장되어 있는 app/static/경로(기본 경로) 및 STATICFILES_DIRS에 정의된 추가 경로들을 탐색
# 실제 파일이나 디렉토리가 아니며, URL로만 존재
# 비어있지 않은 값으로 설정한다면 반드시 slash(/)로 끝나야 함

MEDIA_ROOT = BASE_DIR / 'media'
# 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
# 장고는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음(데이터베이스에 저장되는 것은 "파일 경로")
# 실제 디렉토리 경로, 물리적인 파일경로
# 업로드 하면 자동으로 media 폴더 생김(따로 만들 필요 없음)
# 그 안에 경로 주소가 생김(같은 이름의 파일을 업로드한다면 장고는 임의의 난수값을 붙여 저장함)
# MEDIA_ROOT = BASE_DIR / 'crud/media' 로 바꾸면 crud 폴더 내 media 폴더 생기고 거기에 저장됨

MEDIA_URL = '/media/'
# MEDIA_ROOT에서 제공되는 미디어 파일을 처리하는 URL
# 업로드 된 파일의 주소(URL)를 만들어 주는 역할
# 비어 있지 않은 값으로 설정 한다면 반드시 slash로 끝나야 함
# 제공하기 위한 URL, 물리적인 파일경로가 아니라 URL로만 존재
# MEDIA_URL = '/crud/media/' 로 바꾸면 개발자도구에서 이 루트로 보여짐

# url.py 가서 MEDIA_URL, MEDIA_ROOT 작성하기

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User' 
