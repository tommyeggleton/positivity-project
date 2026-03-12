# web: gunicorn --config gunicorn.conf.py positivity_project.wsgi
web: gunicorn -b $PORT positivity_project.wsgi
release: python manage.py migrate
