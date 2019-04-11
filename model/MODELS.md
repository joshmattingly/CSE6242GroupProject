Output from Running Build Models
================================

This is the latest output from running `build_models.py`. We can see that for different pollutants a different regressor may perform better.


    $ python build_models.py 

    [1] FIND THE BEST MODEL FOR EACH PARAMETER

    ### PM 2.5 ###
      === KNeighborsRegressor ===
        Best Params: {'n_neighbors': 10, 'weights': 'distance'}
        RMSE = 6.121170304265129 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.48988902328317085
      === RandomForestRegressor ===
        Best Params: {'max_depth': None, 'n_estimators': 1000}
        RMSE = 6.219650569582212 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.47334317635808204
      === MLPRegressor ===
        Best Params: {}
        RMSE = 8.211135542514977 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.08208559398821214
      Best RMSE: 6.121170304265129
      Best Model: KNeighborsRegressor
      Best Params:  {'n_neighbors': 10, 'weights': 'distance'}

    ### PM 10 ###
      === KNeighborsRegressor ===
        Best Params: {'n_neighbors': 10, 'weights': 'distance'}
        RMSE = 4.987112845702762 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.06003042565321626
      === RandomForestRegressor ===
        Best Params: {'max_depth': None, 'n_estimators': 1000}
        RMSE = 4.926698219962298 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.03450325582664271
      === MLPRegressor ===
        Best Params: {}
        RMSE = 5.329957255241971 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.21078600494360455
      Best RMSE: 4.926698219962298
      Best Model: RandomForestRegressor
      Best Params:  {'max_depth': None, 'n_estimators': 1000}

    ### Ozone ###
      === KNeighborsRegressor ===
        Best Params: {'n_neighbors': 10, 'weights': 'distance'}
        RMSE = 0.05902416980319624 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.07114326610338362
      === RandomForestRegressor ===
        Best Params: {'max_depth': None, 'n_estimators': 1000}
        RMSE = 0.05837741807702735 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.09138746179356239
      === MLPRegressor ===
        Best Params: {}
        RMSE = 0.0694053904859785 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.2843262625538032
      Best RMSE: 0.05837741807702735
      Best Model: RandomForestRegressor
      Best Params:  {'max_depth': None, 'n_estimators': 1000}

    ### Nitrogen dioxide ###
      === KNeighborsRegressor ===
        Best Params: {'n_neighbors': 10, 'weights': 'distance'}
        RMSE = 0.027759193817792044 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.0003828799092113755
      === RandomForestRegressor ===
        Best Params: {'max_depth': None, 'n_estimators': 100}
        RMSE = 0.026247589923314687 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.10628540220186344
      === MLPRegressor ===
        Best Params: {}
        RMSE = 0.029911164903074012 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.16061089055340383
      Best RMSE: 0.026247589923314687
      Best Model: RandomForestRegressor
      Best Params:  {'max_depth': None, 'n_estimators': 100}

    ### Sufur dioxide ###
      === KNeighborsRegressor ===
        Best Params: {'n_neighbors': 10, 'weights': 'distance'}
        RMSE = 0.6550903318381651 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.11455445812519083
      === RandomForestRegressor ===
        Best Params: {'max_depth': None, 'n_estimators': 1000}
        RMSE = 0.6529079393730673 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.12044424390711571
      === MLPRegressor ===
        Best Params: {}
        RMSE = 0.6974583328383037 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.003681710828894236
      Best RMSE: 0.6529079393730673
      Best Model: RandomForestRegressor
      Best Params:  {'max_depth': None, 'n_estimators': 1000}

    ### Carbon monoxide ###
      === KNeighborsRegressor ===
        Best Params: {'n_neighbors': 5, 'weights': 'distance'}
        RMSE = 8.19832339362624 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.008248842792379696
      === RandomForestRegressor ===
        Best Params: {'max_depth': None, 'n_estimators': 1000}
        RMSE = 8.224141474550294 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.014609177053199527
      === MLPRegressor ===
        Best Params: {}
        RMSE = 8.178588443243498 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.0034005851484728566
      Best RMSE: 8.178588443243498
      Best Model: MLPRegressor
      Best Params:  {}

    ### Hydrogen Sulfide ###
      === KNeighborsRegressor ===
        Best Params: {'n_neighbors': 5, 'weights': 'distance'}
        RMSE = 0.7699813443168771 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.09318747810682138
      === RandomForestRegressor ===
        Best Params: {'max_depth': None, 'n_estimators': 100}
        RMSE = 0.6598700487829433 μg/m^3
        Coefficient of determination R^2 of the prediction = 0.19711919441009806
      === MLPRegressor ===
        Best Params: {}
        RMSE = 0.7379241243281873 μg/m^3
        Coefficient of determination R^2 of the prediction = -0.004055362189710143
      Best RMSE: 0.6598700487829433
      Best Model: RandomForestRegressor
      Best Params:  {'max_depth': None, 'n_estimators': 100}

    DONE.
