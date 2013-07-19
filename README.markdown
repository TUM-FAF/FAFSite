FAF Site
==============

[Official website](http://faf.utm.md/)

What is FAF?
--------------
FAF represents an English Taught Honor's Program in Computer Science at the Technical University of Moldova. Basically we are a group of enthusiastic and proactive students that try their best. 

In order to share things and promote ourselves we decided to lanch our website. 

Installation
-------------
In order to setup and run the project follow the steps:

1. Ensure that you have any Python version from 2.6.5 to 2.7. For this run `python -c 'import sys; print(sys.version_info[:])'`
2. Also you should have pip installed. Run `easy_install pip` or `sudo apt-get install python-pip`
3. Install virtualenv if you don't have one: `pip install virtualenv`
4. After cloning fafsite project, create a virtualenv inside the project and activate it. 


        $ cd fafsite
        $ virtualenv env
        $ source env/bin/activate

5. Run `pip install -r requirements.txt`
6. Copy the stagging settings to a settings file.


        $ cp fafsite/staging_settings.py fafsite/settings.py
     
7. Create the tables in the database: `python manage.py syncdb`. When prompted for a superuser, create one. 
These are the credentials you are going to use for logging in to the admin panel.
8. Run the wsgi server: `python manage.py runserver`
9. Run the tests: `python manage.ry test`. Note: please run the tests everytime you make a change.


Contributing
-----------
For everyone who is willing to contribute please check our [Contribution Guidelines](https://github.com/ana-balica/fafsite/wiki/FAFsite-Contribution-Guidelines).
