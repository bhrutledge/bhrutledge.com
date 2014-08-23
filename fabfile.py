from fabric.api import *
import os

# TODO: Switch to Invoke
# TODO: Move content back to Git?


def dev():
    env.pelican_input = os.path.expanduser('~/Dropbox/bhrutledge.com/content')
    env.pelican_output = os.path.expanduser('~/Sites/bhrutledge')
    env.resume_dir = os.path.expanduser('~/Code/resume')
    env.pelican_conf = 'pelicanconf.py'


def live():
    dev()
    env.pelican_output = os.path.expanduser('~/webapps/bhrutledge')
    env.pelican_conf = 'publishconf.py'


def clean():
    if os.path.isdir(env.pelican_output):
        local('find {pelican_output} -mindepth 1 -delete'.format(**env))


def resume():
    local('cp {resume_dir}/brian-rutledge-resume.html '
          '{pelican_output}/resume.html'.format(**env))
    local('cp {resume_dir}/resume.css {pelican_output}'.format(**env))


def build(pelican_args=''):
    clean()
    env.pelican_args = pelican_args
    local('pelican {pelican_input} -o {pelican_output} -s {pelican_conf} '
          '{pelican_args}'.format(**env))
    resume()
    local('chmod -R a+rX {pelican_output}'.format(**env))


def regen():
    build('-r')

