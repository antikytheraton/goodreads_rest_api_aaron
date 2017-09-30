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