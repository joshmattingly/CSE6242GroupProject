###
# We need to add Zip Code to the output file to work with Livability Scoring!
# Depends On: output.csv
###
import numpy as np
import pandas as pd
from utils import weekends, hods, resolution_lon, resolution_lat, grid_lon, grid_lat

output = pd.read_csv('./data/output.csv')

####
# MAJOR HACK
# Need to match zip codes to the output.csv, floats are pain to match and is causing all kinds of problems.
# Also, I really need a zip code everywhere, not just geocode-able places.
# HACK: Take the previous geocoded lat,lon,zips and use KNN to find the closest zip to any given point
# and use that zip code.
# NOTE: if this was a random data set, this would not work well but because it should be a data set with the
# same lats/lons the accuracy should be good especially since we are using n_neighbors=1
###
from sklearn.neighbors import KNeighborsClassifier
dfJosh = pd.read_csv('./data/chicago_pollutants_by_latlong.csv')
dfLatLonZip = dfJosh[['lat','long','Zip Code']].copy().drop_duplicates(subset=('lat','long')).reset_index()

classifier = KNeighborsClassifier(n_neighbors=1, weights='distance')
classifier.fit(dfLatLonZip[['lat','long']], dfLatLonZip['Zip Code'])

output['Zip Code'] = classifier.predict(output[['lat','long']])

output.to_csv('./data/output_with_zip.csv', index=False)
print('\nDONE.')