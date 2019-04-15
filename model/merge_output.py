###
# Merge the results of the pollutant CSVs into a single CSV that is
# easier to work with.
# Depends on: outputs/*.csv
###

import pandas as pd
import numpy as np
import time
import calendar
import pickle

from utils import max_lon, min_lon, max_lat, min_lat, grid_lon, grid_lat, resolution, build_X_grid

parameters = ['PM 2.5','PM 10','Ozone','Nitrogen dioxide','Sufur dioxide','Carbon monoxide','Hydrogen Sulfide']

print('Merging all outputs into a single file...')
dfJoined = None
for parameter in parameters:
    # weekend,hod,lat,long,z
    dfRaw = pd.read_csv('outputs/{}.csv'.format(parameter), index_col=(0,1,2,3), 
        header=None, skiprows=1, names=('weekend','hod','lat','long',parameter))
    if dfJoined is None:
        dfJoined = dfRaw
    else:
        dfJoined[parameter] = dfRaw[parameter]
dfJoined.to_csv('data/output.csv')

print(' > data/output.csv')
print('DONE.')