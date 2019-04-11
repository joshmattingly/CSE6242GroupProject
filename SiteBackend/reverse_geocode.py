import sys
import pandas as pd
import requests
import json
import time
sys.path.insert(0, '../')

import config

latlong='40.714224,-73.961452'
dataset = pd.read_csv('./static/lat_long_for_lookup.csv')
r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+latlong+'&key=' + config.api_key)

for index, row in dataset.iterrows():
    latlong = str(row['lat']) + ',' + str(row['long'])
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng='+latlong+'&key=' + config.api_key)
    response = json.loads(r.content)

    try:
        for component in response['results'][0]['address_components']:
            if component['types'][0] == 'postal_code':
                zipcode = component['long_name']
            if component['types'][0] == 'locality':
                city = component['long_name']

        dataset.loc[index, 'zipcode'] = zipcode
        dataset.loc[index, 'city'] = city
        print(row['ID'], row['lat'], row['long'], city, zipcode)
    except KeyError:
        pass
    except IndexError:
        dataset.to_csv('./static/geo_coded_pollutants.csv')
    time.sleep(0.5)
