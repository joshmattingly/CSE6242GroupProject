import pandas as pd
import numpy as np
import time
import calendar
import pickle

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from utils import max_lon, min_lon, max_lat, min_lat, build_X_grid, resolution_lon, resolution_lat


parameters = ['PM 2.5','PM 10','Ozone','Nitrogen dioxide','Sufur dioxide','Carbon monoxide','Hydrogen Sulfide']

for parameter in parameters:
    df = pd.read_csv('outputs/{}.csv'.format(parameter))
    data = df[(df.weekend == 0) & (df.hod == 12)]
    avgs = np.reshape(data['z'].values, (resolution_lon, resolution_lat))

    # Plot in 3-d
    fig = plt.figure(figsize=(10,5))
    fig.suptitle('{} at Noon on a Weekday'.format(parameter))
    ax = fig.gca(projection='3d')
    lons = np.reshape(data['long'].values, (100, 100))
    lats = np.reshape(data['lat'].values, (100, 100))
    surf = ax.plot_surface(lons, lats, avgs, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig('charts/{}.png'.format(parameter), bbox_inches='tight')

print('DONE.')