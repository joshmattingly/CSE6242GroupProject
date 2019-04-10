import os
import config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import utilities

test_summary = '''
This portion and only this portion will have a very long text so much so that the vertical scroll bar may appear when 
required. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam congue neque et sollicitudin blandit. Vivamus 
vestibulum sed mauris a volutpat. Etiam quis arcu dictum, scelerisque ex sit amet, egestas eros. Sed convallis 
consectetur mauris, at fringilla mi gravida eu. Vivamus eu sagittis nulla. Vestibulum lobortis pretium metus, ut mattis 
libero aliquet ut. Sed facilisis elementum dolor. Suspendisse euismod nunc malesuada, laoreet lectus egestas, auctor ex. 
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean egestas odio nec ex suscipit vestibulum. Class aptent 
taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nunc bibendum turpis eget erat volutpat, 
vel.
'''


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = config.Config.SECRET_KEY
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


class AddressForm(FlaskForm):
    address = StringField(validators=[DataRequired()])
    submit = SubmitField()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Role=Role, User=User, Data=Data)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddressForm()
    entry = form.address.data
    geo_record = []
    address = '2251 W North Ave Chicago, IL 60647'
    reps = []
    if form.validate_on_submit():
        # entry = form.address.data
        # geo_record = utilities.geocode(entry)
        # reps = utilities.get_reps()
        form.address.data = ''

    return render_template('index.html', api_key=config.api_key, location_score='55%', summary=test_summary,
                           form=form, entry=entry, address=address, reps=reps)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/paper')
def paper():
    return render_template('paper.html')


@app.route('/poster')
def poster():
    return render_template('poster.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
