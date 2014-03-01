import os
from contextlib import contextmanager

from fabric.api import local, env, task, cd


env.directory = os.path.dirname(__file__)
env.activate = ''


@task
def localhost():
    env.run = local
    env.hosts = ['localhost']

# @task
# def remote():
#     env.run = "ana@17324987"


@task
def create_virtualenv(location=""):
    env_path = os.path.join(env.directory, location, 'env')
    env.run("virtualenv {0}".format(env_path))
    activate_path = os.path.join(env_path, 'bin/activate')
    env.activate = "source {0}".format(activate_path)


@task
def install_requirements():
    env.run("env/bin/pip install -r requirements.txt")


@task
def syncdb():
    env.run('python fafsite/manage.py syncdb')
    env.run('python fafsite/manage.py migrate')


@task
def setup(env_location=""):
    env.run('sudo apt-get install python-dev')
    env.run('sudo apt-get install -y python-setuptools')
    env.run('sudo easy_install pip')
    env.run('sudo pip install virtualenv')
    create_virtualenv(env_location)
    install_requirements()
    env.run('sudo apt-get install mysql-server mysql-client libmysqlclient-dev')
    env.run('cp fafsite/fafsite/staging_settings.py fafsite/fafsite/settings.py')
    syncdb()
