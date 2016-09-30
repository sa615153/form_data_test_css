# -*- coding:utf-8 -*-
from flask_wtf import Form
from wtforms import TextField,BooleanField,PasswordField,StringField,SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    user_name = StringField('user name', validators=[DataRequired(), Length(max=15)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me', default=False)
    submit = SubmitField('Login')



