Building the Model
==================

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

Running
-------

Run `python build_model.py` which will generate results in the directories: `./charts/`, `./models/`, and `./outputs/`.

Then to merge all the output files into a single CSV run: `python merge_output.py`.

Generating GeoJSON
------------------

GeoJSON of a filled contour plot.

Run `python do_geojson.py` which will generate a geojson file for every csv in the `./outputs/` directory.

Steps
-----
1. `python build_model.py` - Build the model from the basic inputs
2. `python merge_output.py` - Merge the model results into a single file
3. `python output_zips.py` - Attach zip codes to the results
4. `python livability_csv.py` - Attach livability scores to the resutls
5. `python livability_geojson.py` - Convert to GeoJSON shaded contours for mapping