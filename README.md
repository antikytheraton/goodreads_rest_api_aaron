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