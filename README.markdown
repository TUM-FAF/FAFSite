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

Developing front-end
--------------------
We do use technologies that have to be preprocessed (e.g. Stylus, CoffeeScript).

In order to automate front-end building and keep it cross-platform we use Grunt.js. The structure of folders is as follows:

* _mockup_ - HTML examples of components
* _src/script_ - JS sources (Coffee)
* _src/style_ - CSS sources (Stylus)
* _src/template_ - HTML sources (Handlebars)

In order to be able to build front-end you'll need:

1. Node.js [now to install](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager)
*. Grunt-cli. Run `npm install -g grunt-cli`
*. Go to project folder in your favorite terminal `cd fafsite`
*. Install packages `npm install`
*. Run development task `grunt` or `grunt server`
*. Install [LiveReload](https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei) in Google Chrome
*. Open _localhost/fafsite/mockup/index.html_ in your browser (you need a local server for that)
*. Activate LiveReload in browser

Now any change in sources should recompile the project and reload the browser automatically.

Before commiting stop Grunt task (Ctrl+c) and run `grunt build`. This way files will get optimized and all necessary files will be copied in their right place.


Contributing
-----------
For everyone who is willing to contribute please check our [Contribution Guidelines](https://github.com/ana-balica/fafsite/wiki/FAFsite-Contribution-Guidelines).
