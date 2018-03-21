# -*- coding: utf-8 -*-
from os import environ

__author__ = 'AlexGirin'


class Config(object):
    DEBUG = True
    SECRET_KEY = environ.get('SECRET_KEY') or 'MySecretKey'
    WTF_CSRF_ENABLED = False
