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
