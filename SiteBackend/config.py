import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


api_key = 'AIzaSyCLKuAgHOU70gyFXOl-pLwvyoDbXqU6rxI'
