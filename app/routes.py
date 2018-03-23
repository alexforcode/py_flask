# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User

__author__ = 'AlexGirin'


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'Альберт Эйнштейн'},
            'body': 'Уравнения для меня важнее, потому что политика — для настоящего, а уравнения — для вечности.'
        },
        {
            'author': {'username': 'Стивен Хокинг'},
            'body': 'Если вы понимаете, как функционирует Вселенная, то, в известном смысле, можете ею управлять.'
        },
        {
            'author': {'username': 'Ричард Фейнман'},
            'body': 'Физика подобна сексу: иногда даёт практические результаты, но занимаются ей не поэтому.'
        }
    ]
    return render_template('index.html', title='Главная', posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильный логин или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Регистрация', form=form)
