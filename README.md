#Basic Matcher Assignment
###Hila Rubin

# Requirements

* Python 3.7
* Django 3.2

#Installation
```
python -m venv matcherEnv
matcherEnv\Scripts\activate.bat
pip install -r requirements.txt
```
###That's it, we're done!
```
python manage.py runserver
```
Now you can enter your browser with http://***.*.*.*:8000/matcher/

###### If you want to create your own data:
1. Delete all files in the 'myApp\matcher\migrations' folder
2. Delete the db.sqlite3
3. Run the following code:
```
python manage.py makemigrations matcher
python manage.py migrate
python manage.py runserver
```

