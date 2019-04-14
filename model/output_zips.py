###
# We need to add Zip Code to the output file to work with Livability Scoring!
# Depends On: output.csv
###
import numpy as np
import pandas as pd
from utils import weekends, hods, resolution_lon, resolution_lat, grid_lon, grid_lat

output = pd.read_csv('./data/output.csv')

from sklearn.neighbors import KNeighborsClassifier
dfJosh = pd.read_csv('./data/chicago_pollutants_by_latlong.csv')
dfLatLonZip = dfJosh[['lat','long','Zip Code']].copy().drop_duplicates(subset=('lat','long')).reset_index()

classifier = KNeighborsClassifier(n_neighbors=1, weights='distance')
classifier.fit(dfLatLonZip[['lat','long']], dfLatLonZip['Zip Code'])

output['Zip Code'] = classifier.predict(output[['lat','long']])

output.to_csv('./data/output_with_zip.csv')
print('\nDONE.')