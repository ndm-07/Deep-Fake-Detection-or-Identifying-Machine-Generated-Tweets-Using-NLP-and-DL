@echo off
echo Applying migrations...
python manage.py makemigrations
python manage.py migrate

echo Starting Django development server...
python manage.py runserver

pause
