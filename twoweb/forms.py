#/bin/python
# -*- coding: utf-8 -*-
"""
    :author: huweihua
    :url: http://
    :copyright: © 2020 huweihua <huwihua6@hikvision.com>
    :license:
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(1, 20)])
    host = StringField('Host', validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
