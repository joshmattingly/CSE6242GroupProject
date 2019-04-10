import pandas as pd
import numpy as np
import time
import calendar
import pickle

from utils import max_lon, min_lon, max_lat, min_lat, grid_lon, grid_lat, resolution, build_X_grid

parameters = ['PM 2.5','PM 10','Ozone','Nitrogen dioxide','Sufur dioxide','Carbon monoxide','Hydrogen Sulfide']
print('Latitude Range: {} to {}'.format(min_lat, max_lat))
print('Longitude Range: {} to {}'.format(min_lon, max_lon))

X_grid = build_X_grid()
output = build_X_grid()
for parameter in parameters:
    model = pickle.load(open('{}.pickle'.format(parameter), 'rb'))
    z = model.predict(X)
    output[parameter] = z
output.to_csv('output.csv')