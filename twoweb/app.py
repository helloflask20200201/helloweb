#/bin/python
# -*- coding: utf-8 -*-
"""
    :author: huweihua
    :url: http://
    :copyright: © 2020 huweihua <huwihua6@hikvision.com>
    :license:
"""
from flask import Flask, render_template, flash, redirect, url_for, request, send_from_directory, session
from flask import jsonify,request
from flask_bootstrap import Bootstrap
import json
from twoweb.forms import HelloForm

app = Flask(__name__)
app.secret_key = 'secret string'
bootstrap = Bootstrap(app)
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/contents', methods=['GET', 'POST'])
def contents():
    return render_template('contents.html')

@app.route('/zabbix', methods=['GET', 'POST'])
def zabbix():
    return render_template('zabbix.html')

@app.route('/zabbix_maintain', methods=['GET', 'POST'])
def zabbix_maintain():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        host = form.host.data
        flash('Your message have been sent to the world!')
    return render_template('zabbix/zabbix_maintain.html',form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('error/404.html')

@app.route('/re', methods=['GET', 'POST'])
def re():
    print(request.json,'\n',request.headers)
    print(bytes.decode(request.data))

    if request.data:
        re = bytes.decode(request.data)
        data = json.loads(re)
    else:
        data = {
            'error':'1',
            'message':'data is null'
        }
    return jsonify(data)