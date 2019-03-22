import sys
import pandas as pd
import requests
import json
import time
sys.path.insert(0, '../')

import config

latlong='40.714224,-73.961452'
dataset = pd.read_csv('nodes.csv')
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+latlong+'&key=' + config.API_KEY)

for index, row in dataset.iterrows():
    print(row['node_id'], row['lat'], row['lon'])
    latlong = str(row['lat']) + ',' + str(row['lon'])
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+latlong+'&key=' + config.API_KEY)
    response = json.loads(r.content)
    print(response['results'][0]['address_components'][-1]['long_name'])
    dataset.loc[index, 'zipcode'] = response['results'][0]['address_components'][-1]['long_name']
    time.sleep(1)

dataset.to_csv('out.csv')
