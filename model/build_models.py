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

# download Josh's cleaned data set: https://s3.us-east-2.amazonaws.com/chipy6242/dataset_clean.csv
# df = pd.read_csv('https://s3.us-east-2.amazonaws.com/chipy6242/dataset_clean.csv', parse_dates=['datetime'])
df = pd.read_csv('dataset_clean.csv', parse_dates=['datetime'])

# Input Parameters we are looking at (with filtering on the dataframe)
parameters = [
  ('PM 2.5', (df.parameter == 'pm2_5')),
  ('PM 10', (df.subsystem=='alphasense') & (df.sensor == 'opc_n2') & (df.parameter == 'pm10')),
  ('Ozone', (df.subsystem=='chemsense') & (df.sensor == 'o3') & (df.parameter == 'concentration')), # o3
  ('Nitrogen dioxide', (df.subsystem=='chemsense') & (df.sensor == 'no2') & (df.parameter == 'concentration')), #no2
  ('Sufur dioxide', (df.subsystem=='chemsense') & (df.sensor == 'so2') & (df.parameter == 'concentration')), # so2
]

# Models to test
models = [ # list of tuples of (ModelClass, grid-searchable hyperparameters dictionary)
    (KNeighborsRegressor, { 'n_neighbors': [3, 5, 10], 'weights': ['distance'] }),
    (RandomForestRegressor, { 'n_estimators': [100, 1000], 'max_depth': [None] }),
]

for (name, df_filter) in parameters:
    print('### {} ###'.format(name))
    # Create the independent variables
    X = df[df_filter]
    X = X[['datetime','lat','long']]
    X['hod'] = X['datetime'].apply(lambda x: x.hour)
    X['dow'] = X['datetime'].apply(lambda x: x.dayofweek)
    X = X[['hod','lat','long']]

    # Create the predicted variable
    y = df[df_filter]
    y = y['avg']

    # Split the data into a Training and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, shuffle=True)

    # Find the best model for this parameter
    bestRMSE = None
    bestGridSearch = None
    for (model, params) in models:
        # Grid Search for the best hyper parameters
        print('  === {} ==='.format(model.__name__))
        gridSearch = GridSearchCV(model(), param_grid=params, refit=True)
        gridSearch.fit(X_train, y_train)
        print('    Best Params:', gridSearch.best_params_)

        # Check its accuracy by looking at the Root Mean Square Error of the KNN on the Test dataset
        y_pred = gridSearch.predict(X_test)
        dfTest = pd.DataFrame([y_pred, y_test]).transpose()
        dfTest.columns=('p','y')
        rmse = ((dfTest.p - dfTest.y) ** 2).mean() ** .5
        print('    RMSE = {} μg/m^3'.format(rmse))
        score = gridSearch.score(X_test, y_test)
        print('    Coefficient of determination R^2 of the prediction = {}'.format(score))

        if bestRMSE is None or rmse < bestRMSE:
            bestRMSE = rmse
            bestGridSearch = gridSearch

    print('  Best RMSE: {}'.format(bestRMSE))
    print('  Best Model: {}'.format(type(bestGridSearch.best_estimator_).__name__))
    print('  Best Params: ',bestGridSearch.best_params_)
    print()

    # Setup the BEST model for this indicator
    model = bestGridSearch.best_estimator_
    model.fit(X, y)
    pickle.dump(model, open('{}.pickle'.format(name), 'wb'))

    # Build the Grid to interpolate over
    max_lat = X['lat'].min()
    min_lat = X['lat'].max()
    max_lon = X['long'].min()
    min_lon = X['long'].max()
    print('Latitude Range: {} to {}'.format(min_lat, max_lat))
    print('Longitude Range: {} to {}'.format(min_lon, max_lon))

    hod = 12 # NOON
    resolution_lon = 100
    resolution_lat = 100

    resolution = resolution_lon * resolution_lat
    grid_lon = np.linspace(min_lon, max_lon, resolution_lon)
    grid_lat = np.linspace(min_lat, max_lat, resolution_lat)

    # Build an array with 2 columns that consists of every combination of the lat/lon's in the interpolation grid
    grid_lon_lat = np.reshape(np.asarray(np.meshgrid(grid_lon, grid_lat)), (2, resolution))
    data = np.zeros((resolution, 3))
    data[:, 0] = hod
    data[:, 2] = grid_lon_lat[0,:]
    data[:, 1] = grid_lon_lat[1,:]
    X_grid = pd.DataFrame(data=data, columns=['hod', 'lat', 'long'])

    # Interpolate over the grid
    z = model.predict(X_grid)
    avgs = np.reshape(z, (resolution_lon, resolution_lat))

    # Plot in 3-d
    fig = plt.figure(figsize=(10,5))
    fig.suptitle('{} at Noon'.format(name))
    ax = fig.gca(projection='3d')
    lons = np.reshape(grid_lon_lat[0], (100, 100))
    lats = np.reshape(grid_lon_lat[1], (100, 100))
    surf = ax.plot_surface(lons, lats, avgs, 
                           cmap=cm.coolwarm, linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.savefig('{}.png'.format(name), bbox_inches='tight')

print('DONE.')