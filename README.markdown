FAF Site
==============

What is FAF?
--------------
FAF represents an English Taught Honor's Program in Computer Science at the Technical University of Moldova. Basically we are a group of enthusiastic and proactive students that try their best. 

In order to share things and promote ourselves we decided to lanch our website. 

Set Up
-------------
In order to run the project follow the steps:

1.   Install Python 2.5 or higher (we are using [Python 2.7](http://www.python.org/getit/))
2.   Download and set up [Django 1.4.1](https://www.djangoproject.com/download/)
3.   Install [django-TinyMCE](https://github.com/aljosa/django-tinymce)
4.   Instal MySQL
5.   Install python-mysqldb
6.   Run the following
     + `mysql -u root -p`
     + `mysql> CREATE DATABASE fafdb;`
     + `mysql> GRANT ALL ON fafdb.* TO 'root'@'localhost' IDENTIFIED BY 'dev';`
     + `mysql> quit`
7.   Install [GIT](http://git-scm.com/), for windows there is GITHUB for Windows
8.   Use GIT to clone fafsite project to your local directory 
9.   cd to the project path and run the following `<python manage.py syncdb>`
10.   Run the project from the console within the project directory `<python manage.py runserver>`
11.   Now you can acces the server on the localhost

Set Up for Ubuntu (dummy style)
-------------

1.   Python is installed by default on Ubuntu (so nothing to do here)
2.   Install pip (`sudo apt-get install python-pip`)
3.   Install Django (`sudo pip install Django`)
4.   Install tiny mce (`sudo pip install django-tinymce`)
5.   Install MySQL (`sudo apt-get install mysql-server`)
6.   Install Python MySQL module (`sudo apt-get install python-mysqldb`)
7.   Open the terminal and run the following 
     + `mysql -u root -p`
     + `mysql> CREATE DATABASE fafdb;`
     + `mysql> GRANT ALL ON fafdb.* TO 'root'@'localhost' IDENTIFIED BY 'dev';`
     + `mysql> quit`
8.   Install git (`sudo apt-get git-core`)
9.   Copy project to your local directory (`git clone https://github.com/ana-balica/fafsite.git`)
10.   cd in fafsite directory (`cd fafsite/`)
11.   Run server (`python manage.py syncdb`)
12.   Run server (`python manage.py runserver`)
