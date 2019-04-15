###
# Shared variables and functions used between other scripts
###

import numpy as np
import pandas as pd

max_lon = -87.934711
min_lon = -87.526155
max_lat = 42.022810
min_lat = 41.644818


resolution_lon = 100
resolution_lat = 100
resolution = resolution_lon * resolution_lat

grid_lon = np.linspace(min_lon, max_lon, resolution_lon)
grid_lat = np.linspace(min_lat, max_lat, resolution_lat)
weekends = np.arange(2)
hods = np.arange(24)

# Build an array with 2 columns that consists of every combination of the lat/lon's in the interpolation grid
# grid_lon_lat = np.reshape(np.asarray(np.meshgrid(grid_lon, grid_lat)), (2, resolution))

def build_X_grid():
    data = np.array(np.meshgrid(weekends, hods, grid_lat, grid_lon)).T.reshape(-1,4)
    X_grid = pd.DataFrame(data=data, columns=['weekend', 'hod', 'lat', 'long'])
    return X_grid[['weekend','hod','lat','long']]