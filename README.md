# Deploy to Heroku and AWS

```bash
$ pip install gunicorn dj-database whitenoise

pip freeze > requirements.txt
```
Proctile
runtime.txt

## separar settings
- base
- local
- production

wsgi con django whitenoise

```bash
heroku login
heroku create goodreads-devf-aaron
heroku open
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku run python manage.py loaddata author.json
heroku run python manage.py loaddata books.json
```
## para deployear un branch de git al master de heroku
```bash
$ git push heroku dev:master
```

## connecting to aws ec2 ubuntu server

- https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Instances:sort=instanceId

```bash
$ sudo cp Downloads/devf-batch16.pem .ssh
$ ssh -i "devf-batch16.pem" ubuntu@ec2-34-209-190-102.us-west-2.compute.amazonaws.com
```


# AWS

https://github.com/antikytheraton/django-deploy-starter-kit

./manage.py migrate --settings=goodreads.settings.production
./manage.py collectstatic --settings=goodreads.settings.production

```bash
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn
$ sudo systemctl enable gunicorn
$ sudo systemctl status gunicorn

$ sudo vim /etc/nginx/sites-available/api
```

# Jenkins
- github integration plugin
- slack notification plugin

```bash
#!/bin/bash
$ source /home/ubuntu/goodreads/entorno/bin/activate
$ cd /var/lib/jenkins/workspace/Goodreads
$ export DJANGO_SETTINGS_MODULE=goodreads.settings.production
$ export SECRET_KEY=of2yq436mgcbhvgs4sp5r2xhc4f68uffd
$ export DB_NAME=good_db
$ export DB_USER=good_admin
$ export DB_PASSWORD=good2017
$ pip install -r requirements.txt           # Install or upgrade dependencies
$ python manage.py migrate --settings=goodreads.settings.production               # Apply South's database migrations
$ python manage.py collectstatic --noinput --settings=goodreads.settings.production  # Collect static files
```



# Holi de nuevo AWS


- lol