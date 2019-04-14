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
from sklearn.neural_network import MLPRegressor
from sklearn.gaussian_process import GaussianProcessRegressor

from utils import max_lon, min_lon, max_lat, min_lat, build_X_grid, resolution_lon, resolution_lat

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
  ('Carbon monoxide', (df.subsystem=='chemsense') & (df.sensor == 'co') & (df.parameter == 'concentration')), # co
  ('Hydrogen Sulfide', (df.subsystem=='chemsense') & (df.sensor == 'h2s') & (df.parameter == 'concentration')), # h2s
]

# Models to test
models = [ # list of tuples of (ModelClass, grid-searchable hyperparameters dictionary)
    (KNeighborsRegressor, { 'n_neighbors': [3, 5, 10], 'weights': ['distance'] }),
    (RandomForestRegressor, { 'n_estimators': [100, 1000], 'max_depth': [None] }),
    # (GaussianProcessRegressor, {}),
    # (LinearRegression, {}),
    (MLPRegressor, {}),
]

print()
print('[1] FIND THE BEST MODEL FOR EACH PARAMETER')
print()

for (name, df_filter) in parameters:
    print('### {} ###'.format(name))
    # Create the independent variables
    X = df[df_filter]
    X = X[['datetime','lat','long']]
    X['hod'] = X['datetime'].apply(lambda x: x.hour)
    X['weekend'] = X['datetime'].apply(lambda x: 0 if x.dayofweek < 5 else 1)
    X = X[['weekend','hod','lat','long']]

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
        gridSearch = GridSearchCV(model(), param_grid=params, refit=True, n_jobs=-1)
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
    print('  Best Params: ', bestGridSearch.best_params_)
    print()

    # Setup the BEST model for this indicator
    model = type(bestGridSearch.best_estimator_)(**bestGridSearch.best_params_)
    model.fit(X, y)
    pickle.dump(model, open('models/{}.pickle'.format(name), 'wb'))


    # Interpolate over the grid
    X_grid = build_X_grid()
    z = model.predict(X_grid)
    output = build_X_grid()
    output['z'] = z
    output.to_csv('outputs/{}.csv'.format(name), index=False)

    # Reshape data for plot'n
    data = output[(output.weekend == 0) & (output.hod == 12)]
    avgs = np.reshape(data['z'].values, (resolution_lon, resolution_lat))

    # Plot in 3-d
    fig = plt.figure(figsize=(10,5))
    fig.suptitle('{} at Noon on a Weekday'.format(name))
    ax = fig.gca(projection='3d')
    lons = np.reshape(data['long'].values, (100, 100))
    lats = np.reshape(data['lat'].values, (100, 100))
    surf = ax.plot_surface(lons, lats, avgs, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.savefig('charts/{}.png'.format(name), bbox_inches='tight')

print('DONE.')