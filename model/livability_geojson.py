###
# Generate GeoJson contour plots for the Livability score
# Depends on: data/livability_scores.csv
###
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import geojsoncontour

from utils import weekends, hods, resolution_lon, resolution_lat, grid_lon, grid_lat

n_contours = 50
parameter = 'Livability'
output = pd.read_csv('./data/livability_scores.csv')
for weekend in weekends:
    for hod in hods:
        data = output[(output.weekend == weekend) & (output.hod == hod)]
        avgs = np.reshape(data[parameter].values, (resolution_lon, resolution_lat))
        lons = np.reshape(data['long'].values, (resolution_lon, resolution_lat))
        lats = np.reshape(data['lat'].values, (resolution_lon, resolution_lat))

        z_min = np.nanmin(data[parameter].values)
        z_max = np.nanmax(data[parameter].values)
        z_eql = np.equal(round(z_min, 5), round(z_max, 5))

        if z_eql:
            print('  Cannot plot {}-weekend-{}-hod-{} because there is no variation in the data.'.format(parameter, weekend, hod))
            continue
        levels = np.linspace(start=z_min, stop=z_max, num=n_contours)

        figure = plt.figure()
        ax = figure.add_subplot(111)

        # Try different coloring maps such as: plt.cm.viridis
        # @see https://matplotlib.org/tutorials/colors/colormaps.html
        contourf = ax.contourf(lons, lats, avgs, levels=levels, cmap=plt.cm.jet)

        geojson = geojsoncontour.contourf_to_geojson(
            contourf=contourf,
            min_angle_deg=None,
            ndigits=None,
            stroke_width=0,
            fill_opacity=0.5
        )

        plt.close(figure)

        directory = 'geojsons/contours-{}'.format(n_contours)
        os.makedirs(directory, exist_ok=True)
        name = 'geojsons/contours-{}/{}-weekend-{}-hod-{}.json'.format(n_contours, parameter, weekend, hod)
        file = open(name, 'w')
        file.write(geojson)
        file.close()
        print('Finished: {}'.format(name))
print('DONE.')