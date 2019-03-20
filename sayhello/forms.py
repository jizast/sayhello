# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, Label
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()


#用户类
class Register(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1,20)])
    passwd = PasswordField('请输入密码', validators=[DataRequired(), Length(6,200)])
    Tpasswd = PasswordField('请再次输入密码', validators=[DataRequired(), Length(6,200)])
    submit = SubmitField()


class Login(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1,20)])
    passwd = PasswordField('请输入密码', validators=[DataRequired(), Length(6,200)])
    submit = SubmitField()

class Logined(FlaskForm):
    body = StringField('信息框', validators=[DataRequired(), Length(1,20)])
    submit = SubmitField()