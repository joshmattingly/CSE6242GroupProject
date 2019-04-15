Building the Model
==================

DESCRIPTION
-----------
This package creates a geo-spatial interpolation model of the air pollution data within
Chicago. It analyzes several models and hyperparameters for each pollutant and then 
calculates a livability score from the results. It also predicts over a grid and converts
to a smoother contour plot and outputs geojson for loading on top of a map.

Chosen Parameters to analyze:
* PM 2.5
* PM 10
* Ozone
* Nitrogen dioxide
* Sufur dioxide
* Carbon monoxide
* Hydrogen Sulfide

Chosen algorithms to analyze:
* KNeighborsRegressor
* RandomForestRegressor
* MLPRegressor

Goal: Find the best model for each parameter and make predictions for each hour of the day.

INSTALLATION
------------
* Requires Python 3.5+
* Requeires the following python packages: pandas, numpy, matplotlib, sklearn, geojsoncontour

EXECUTION
---------
The following steps will generate the models, the predictive results, and geojson necessary for 
plotting the predictions on a map. This will take several hours to run from start to finish.

1. `python build_model.py` - Build the model from the basic inputs
2. `python merge_output.py` - Merge the model results into a single file
3. `python output_zips.py` - Attach zip codes to the results
4. `python livability_csv.py` - Attach livability scores to the resutls
5. `python livability_geojson.py` - Convert to GeoJSON shaded contours for mapping
