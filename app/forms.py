# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

__author__ = 'AlexGirin'


class LoginForm(FlaskForm):
    username = StringField('Логин', [
        DataRequired(message='Это поле обязательно.')
    ])
    password = PasswordField('Пароль', [
        DataRequired(message='Это поле обязательно.')
    ])
    remember_me = BooleanField('Запомнить?')
    submit = SubmitField('Вход')


class RegistrationForm(FlaskForm):
    username = StringField('Логин', [
        DataRequired(message='Это поле обязательно.')
    ])
    email = StringField('Email', [
        DataRequired(message='Это поле обязательно.'),
        Email(message='Неверный формат')
    ])
    password = PasswordField('Пароль', [
        DataRequired(message='Это поле обязательно.')
    ])
    password_confirm = PasswordField('Повторите пароль', [
        DataRequired(message='Это поле обязательно.'),
        EqualTo('password', message='Пароли должны совпадать.')
    ])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Такое имя пользователя уже существует.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Такой email уже существует.')


class EditProfileForm(FlaskForm):
    username = StringField('Логин', [
        DataRequired()
    ])
    about_me = TextAreaField('Обо мне', [
        Length(min=0, max=140)
    ])
    submit = SubmitField('Подтвердить')
