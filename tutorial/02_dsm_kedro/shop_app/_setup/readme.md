# Setup docker for django with postgresql

## Create project

```sh
cp -r * ..
cd ..
docker-compose run app1 django-admin startproject myproject .
sudo chown -R $USER:$USER .
```

## re-create project

```sh
docker-compose down --remove-orphans
```

## django create app
```python
docker-compose run app1 python manage.py startapp myapp
```

## django setting
```python
#app1/code/sittings.py

ALLOWED_HOSTS = [*]

INSTALLED_APPS = [
    ...
    'myapp',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db1',
        'PORT': 5432,
    }
}
```

#