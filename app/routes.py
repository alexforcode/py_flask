# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

__author__ = 'AlexGirin'


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Александр'}
    posts = [
        {
            'author': {'username': 'Альберт Эйнштейн'} ,
            'body': 'Уравнения для меня важнее, потому что политика — для настоящего, а уравнения — для вечности.'
        },
        {
            'author': {'username': 'Стивен Хокинг'} ,
            'body': 'Если вы понимаете, как функционирует Вселенная, то, в известном смысле, можете ею управлять.'
        },
        {
            'author': {'username': 'Ричард Фейнман'} ,
            'body': 'Физика подобна сексу: иногда даёт практические результаты, но занимаются ей не поэтому.'
        }
    ]
    return render_template('index.html', title='Главная', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Логин: {}, Запомнить: {}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Вход', form=form)
