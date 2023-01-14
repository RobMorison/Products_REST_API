# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o6m5u@heyxxut-m^!!2f76vwf*0jqby)e!mbk3elv%3i)t-757'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Football1!'
    }
}