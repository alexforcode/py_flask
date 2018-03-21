# -*- coding: utf-8 -*-
from flask import Flask
from config import Config

__author__ = 'AlexGirin'

app = Flask(__name__)
app.config.from_object(Config)

from app import routes