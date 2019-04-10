$ python build_models.py 
### PM 2.5 ###
  === KNeighborsRegressor ===
    Best Params: {'n_neighbors': 10, 'weights': 'distance'}
    RMSE = 6.054989394683159 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.4927660649998156
  === RandomForestRegressor ===



    Best Params: {'max_depth': None, 'n_estimators': 1000}
    RMSE = 6.153808665197447 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.476074537536703
  Best RMSE: 6.054989394683159
  Best Model: KNeighborsRegressor
  Best Params:  {'n_neighbors': 10, 'weights': 'distance'}

Latitude Range: 41.983275 to 41.7052
Longitude Range: -87.52757 to -87.78208166700001
### PM 10 ###
  === KNeighborsRegressor ===
    Best Params: {'n_neighbors': 10, 'weights': 'distance'}
    RMSE = 4.352744472189346 μg/m^3
    Coefficient of determination R^2 of the prediction = -0.18141028203836984
  === RandomForestRegressor ===
    Best Params: {'max_depth': None, 'n_estimators': 1000}
    RMSE = 4.121544240600974 μg/m^3
    Coefficient of determination R^2 of the prediction = -0.05923990286857949
  Best RMSE: 4.121544240600974
  Best Model: RandomForestRegressor
  Best Params:  {'max_depth': None, 'n_estimators': 1000}

Latitude Range: 41.751142 to 41.751142
Longitude Range: -87.71299 to -87.71299
### Ozone ###
  === KNeighborsRegressor ===
    Best Params: {'n_neighbors': 3, 'weights': 'distance'}
    RMSE = 0.06429770056632374 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.0934282881040801
  === RandomForestRegressor ===
    Best Params: {'max_depth': None, 'n_estimators': 1000}
    RMSE = 0.06442704529661507 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.08977720210618556
  Best RMSE: 0.06429770056632374
  Best Model: KNeighborsRegressor
  Best Params:  {'n_neighbors': 3, 'weights': 'distance'}

Latitude Range: 41.968757 to 41.66607800000001
Longitude Range: -87.536509 to -87.745817
### Nitrogen dioxide ###
  === KNeighborsRegressor ===
    Best Params: {'n_neighbors': 10, 'weights': 'distance'}
    RMSE = 0.021450126220826784 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.01695226337848532
  === RandomForestRegressor ===
    Best Params: {'max_depth': None, 'n_estimators': 1000}
    RMSE = 0.02024951941024252 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.12391883348923549
  Best RMSE: 0.02024951941024252
  Best Model: RandomForestRegressor
  Best Params:  {'max_depth': None, 'n_estimators': 1000}

Latitude Range: 41.968757 to 41.66607800000001
Longitude Range: -87.536509 to -87.745817
### Sufur dioxide ###
  === KNeighborsRegressor ===
    Best Params: {'n_neighbors': 10, 'weights': 'distance'}
    RMSE = 0.41957344069412067 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.1679319979685162
  === RandomForestRegressor ===
    Best Params: {'max_depth': None, 'n_estimators': 1000}
    RMSE = 0.3960935565440302 μg/m^3
    Coefficient of determination R^2 of the prediction = 0.2584534857092453
  Best RMSE: 0.3960935565440302
  Best Model: RandomForestRegressor
  Best Params:  {'max_depth': None, 'n_estimators': 1000}

Latitude Range: 41.994597 to 41.66607800000001
Longitude Range: -87.536509 to -87.745817
DONE.