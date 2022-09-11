python manage.py migrate --noinput
python manage.py collectstatic --no-input
gunicorn --workers=2 --bind=0.0.0.0:8000 negrucoin.wsgi:application