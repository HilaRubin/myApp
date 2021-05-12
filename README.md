# Basic Matcher Assignment
A Django web app for matching candidates for relevant jobs.

By Hila Rubin

## Requirements

* Python 3.7
* Django 3.2

## Installation 
For Windows open cmd (run as administrator):
```
1. git clone https://github.com/HilaRubin/myApp
2. cd myApp
3. python -m venv matcherEnv
4. matcherEnv\Scripts\activate.bat
5. pip install -r requirements.txt
6. python manage.py runserver
```

## That's it, we're done!
Now you can enter your browser with http://localhost:8000/matcher/


## *If you want to create your own data:
1. Delete all files in the 'myApp\matcher\migrations' folder
2. Delete the db.sqlite3
3. Run the following code:
      ```
      python manage.py makemigrations matcher
      python manage.py migrate
      python manage.py runserver
      ```

