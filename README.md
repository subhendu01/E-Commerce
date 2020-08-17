## e-commerce
### Create Django project
step-1 : Install django using bellow command
            **_pip install Django_**
step-2 : Check Django version
            **_django-admin --version_**
step-3: Create django project             
            **_django-admin startproject <project_name>_**
                           or
            **_django-admin startproject <project_name> ._**
step-4: To run your application goto you project directory then type
            **_python manage.py runserver_**
        It will run on default port i.e 8000. To change your port you can run yor project as
            **_python manage.py runserver 0.0.0.0:<available_port>_** (port like 8080,5000,3000)
                            or
            **_python manage.py runserver 0:<available_port>_**
step-5: Create database
            **_python manage.py makemigrations_** (if any changes have done in table then it will reflect)
            **_python manage.py migrate_**
step-6: You can check you database here by importing db.sqlite3
            _https://sqliteonline.com/_
step-7: Create Admin user-login
            **_python manage.py createsuperuser_**
step-8: Create an app/page
            **_django-admin startapp <app/page_name>**_            
step-9: Add your app/page in setting.py under INSTALLED_APPS 
         
step-10: Create Model
            
