from fabric.api import *
import os


env.pelican_input = os.path.expanduser('~/Dropbox/bhrutledge.com/content')
env.pelican_output = os.path.expanduser('~/Sites/bhrutledge')
env.pelican_conf = 'pelicanconf.py'
env.pelican_args = ''


def clean():
    if os.path.isdir(env.pelican_output):
        local('find {pelican_output} -mindepth 1 -delete'.format(**env))


def build():
    local('pelican {pelican_input} -o {pelican_output} -s {pelican_conf} '
          '{pelican_args}'.format(**env))


def rebuild():
    clean()
    build()


def regenerate():
    with settings(pelican_args='-r'):
        rebuild()


def publish():
    with settings(pelican_output=os.path.expanduser('~/webapps/pelican'),
                  pelican_conf='publishconf.py'):
        rebuild()
        local('chmod -R a+rX {pelican_output}'.format(**env))
