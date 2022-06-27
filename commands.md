# Commands

- Start Virtual Environnement - `source myenv/Scripts/activate`
- Start Web Server - `py manage.py runserver`
- Create new app - `py manage.py startapp [appName]`
- update database models - `py manage.py makemigrations [appName]`, `py manage.py migrate [appName]`
- add environment variable - `set -a; source /d/DSUsers/uie50320/wednesday/jofrid/.env; set +a`    
- python anywhere virtual env - `workon <your-pythonanywhere-domain>.pythonanywhere.com` 
- sync static files - `python manage.py collectstatic`

## Create
- Add new app(inside virtual environment) - `py manage.py startapp <appName>`