# -*- coding: utf-8 -*-

from fabric.api import local, run, env

env.hosts = ['deploy@115.29.34.177']


def prepare():
    local('git pull origin master')


def publish():
    local('gitbook build')
    local('git add . && git commit')
    local('git push origin master')
    run('cd /home/deploy/projects/flyingjay-gitbooks && git pull')
