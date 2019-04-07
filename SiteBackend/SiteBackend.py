import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Data(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    zipcode = db.Column(db.Text)
    subsystem = db.Column(db.Text)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)
    sensor = db.Column(db.Text)
    parameter = db.Column(db.Text)
    datetime = db.Column(db.DateTime)
    avg = db.Column(db.Float)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Role=Role, User=User, Data=Data)


@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
