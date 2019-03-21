import sys
import pandas as pd
sys.path.insert(0, '../')

import config

# latlong=40.714224,-73.961452
dataset = pd.read_csv('nodes.csv')
geo_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng='+latlong+'&key=' + config.API_KEY
