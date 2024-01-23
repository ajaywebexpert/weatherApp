Run migrations to apply changes:

python manage.py makemigrations
python manage.py migrate

Run the deployment server
python manage.py runserver


Visit http://127.0.0.1:8000/api/signup/ to create a new user,
http://127.0.0.1:8000/api/login/ to log in, 
http://127.0.0.1:8000/api/weather/search/ to perform a weather search.

Please replace placeholder values with your actual AccuWeather API key
