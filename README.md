# minxful_CST438_Project-


## Requirements

* python 3.8
* postgres
* psycopg


Look at the database section in settings.py to get name of db to create. To run, create a db with the same name and make sure the user is correct.


### Admin User

The admin User info

Username:rosario 

Password: 123456 

# 12/1/19 - Rosario

The posts are now being displayed onto the html page. This is being done by creating them through admin and then displaying them.

Created a snippet function to only show a part of the post this is handly for longer posts.

You guys can use this login to check things the database tables. The tables are located in Models. The Post and Reply are the only tables that are included as of now

Have created the assets folder to help with css, it's not working and i think it could be because of debug not sure though.

Also, i did notice the time of the database is off. We need to fix that.

I need to fix the  path('forum', include('forum.urls')), this is not working. I have no idea why!

# 12/7/19 - Pernille 

To be able to run the application bootstrap much be installed. When the enviorment is active run this command: 
pip install django-crispy-forms

Make sure setting.py have this: 

INSTALLED_APPS = [
    ...

    'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
