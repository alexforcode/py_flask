# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators

__author__ = 'AlexGirin'


class LoginForm(FlaskForm):
    username = StringField('Логин', [
        validators.DataRequired(message='Это поле обязательно.')
    ])
    password = PasswordField('Пароль', [
        validators.DataRequired(message='Это поле обязательно.')
    ])
    remember_me = BooleanField('Запомнить?')
    submit = SubmitField('Вход')
