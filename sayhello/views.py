# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import flash, redirect, url_for, render_template, session

from sayhello import app, db
from sayhello.forms import HelloForm, Register, Login, Logined
from sayhello.models import Message, User


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
#    form = HelloForm()
    if session['logged_in']:
        form = Logined()
        if form.validate_on_submit():
            name = session['username']
            body = form.body.data
            message = Message(body=body, name=name)
            db.session.add(message)
            db.session.commit()
            flash('信息已发布!')
            return redirect(url_for('index'))
    else:
        flash('什么奇怪问题！')
    return render_template('index.html', form=form, messages=messages)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        username = form.username.data
        password = form.passwd.data
        Tpassword = form.Tpasswd.data
        if password == Tpassword:
            user = User(username=username, password=password)
            if User.query.filter_by(username=username).first():
                flash('用户名已存在！')
            else:
                db.session.add(user)
                db.session.commit()
                flash('注册成功!')
            return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login()
    edform = Logined()
    if form.validate_on_submit():
        urname = form.username.data
        passwd = form.passwd.data
        dbpassword = User.query.filter_by(username=urname).first().password
        if dbpassword == passwd:
            flash('登录成功！')
            session['logged_in'] = True
            session['username'] = urname
        else:
            flash('密码不正确或者用户不存在')
        return redirect(url_for('index'))            
    return render_template('login.html', form=form)

