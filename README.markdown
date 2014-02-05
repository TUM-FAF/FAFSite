FAF Site
==============

[Official website](http://faf.utm.md/)

What is FAF?
--------------
FAF represents an English Taught Honor's Program in Computer Science at the Technical University of Moldova. Basically we are a group of enthusiastic and proactive students that try their best.

In order to share things and promote ourselves we decided to launch our website.

Installation
-------------
In order to setup and run the project follow the steps:

1. Ensure that you have any Python version from 2.6.5 to 2.7. For this run `python -c 'import sys; print(sys.version_info[:])'`
*  Also you should have pip installed. Run `easy_install pip` or `sudo apt-get install python-pip`
*  Install virtualenv if you don't have one: `pip install virtualenv`
*  Clone project `git clone git@github.com:ana-balica/fafsite.git`
*  After cloning fafsite project, create a virtualenv inside the project and activate it.


        $ cd fafsite
        $ virtualenv env
        $ source env/bin/activate
*  Run `pip install -r requirements.txt`
*  Set up MySQL on your machine. Make sure that you have `mysql_config`. If you encouter an error that says that `mysql_config` not found, then you must install `libmysqlclient-dev` for debian systems.
*  Install system wide [tinymce](http://www.tinymce.com/) - a web based JavaScript HTML WYSIWYG editor.
*  Copy the stagging settings to the settings file.


        $ cp fafsite/fafsite/staging_settings.py fafsite/fafsite/settings.py
*  Create the tables in the database: `python fafsite/manage.py syncdb`. When prompted for a superuser, create one.
These are the credentials you are going to use for logging in to the admin panel.
*  Run the wsgi server: `python fafsite/manage.py runserver`
*  Run the tests: `python fafsite/manage.py test`. Note: please run the tests every time you make a change.


Developing front-end
--------------------
We do use technologies that have to be preprocessed (e.g. Stylus, LESS< CoffeeScript).

In order to automate front-end building and keep it cross-platform we use [Gulp.js](http://gulpjs.com/). The structure of folders is as follows:

* _src/components_ - Used components (e.g. Bootstrap and jQuery)
* _src/script_ - JS sources (Coffee)
* _src/style_ - CSS sources (Stylus)
* _src/style/bootstrap_ - Bootstrap overriding (LESS)

In order to be able to build front-end you'll need:

1. Node.js [how to install](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager)
*  Install Gulp globally (one time) `npm install -g gulp gulp-util`
*  Install Bower globally (one time) `npm insatll -g bower`
*  Go to project folder in your favorite terminal `cd fafsite`
*  Install packages `npm install`
*  Install bower components `bower install`
*  Run `gulp development` for development version
*  Run `gulp build` for build version

In order to recompile sources live you'll need:
1. Install [LiveReload](https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei) in Google Chrome
*  Run development watch task `gulp w` or `gulp watch`
*  Start python server `python fafsite/manage.py runserver`
*  Open the page in browser
*  Activate LiveReload in browser

Now any change in sources should recompile the project front-end and reload the browser automatically.

Before commiting stop Gulp task (Ctrl+c) and run `gulp build`. This way project will be prepaired for production.


Contributing
-----------
For everyone who is willing to contribute please check our [Contribution Guidelines](https://github.com/ana-balica/fafsite/wiki/FAFsite-Contribution-Guidelines).
