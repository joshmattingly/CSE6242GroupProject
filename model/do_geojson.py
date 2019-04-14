import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import geojsoncontour

from utils import weekends, hods, resolution_lon, resolution_lat, grid_lon, grid_lat

parameters = ['PM 2.5','PM 10','Ozone','Nitrogen dioxide','Sufur dioxide','Carbon monoxide','Hydrogen Sulfide']

output = pd.read_csv('output.csv')

for weekend in weekends:
    for hod in hods:
        data = output[(output.weekend == weekend) & (output.hod == hod)]
        for parameter in parameters:
            avgs = np.reshape(data[parameter].values, (resolution_lon, resolution_lat))
            lons = np.reshape(data['long'].values, (resolution_lon, resolution_lat))
            lats = np.reshape(data['lat'].values, (resolution_lon, resolution_lat))

            n_contours = 10
            z_min = np.nanmin(data[parameter].values)
            z_max = np.nanmax(data[parameter].values)
            z_eql = np.equal(round(z_min, 5), round(z_max, 5))
            # print('  Min = {}, Max = {}, Min==Max = {}'.format(z_min, z_max, z_eql))
            if z_eql:
                print('  Cannot plot {}-weekend-{}-hod-{} because there is no variation in the data.'.format(parameter, weekend, hod))
                continue
            levels = np.linspace(start=z_min, stop=z_max, num=n_contours)

            figure = plt.figure()
            ax = figure.add_subplot(111)

            # surf = ax.plot_surface(lons, lats, avgs, cmap=cm.coolwarm, linewidth=0, antialiased=False)
            # plt.savefig('plots/{}-weekend-{}-hod-{}.png'.format(parameter, weekend, hod), bbox_inches='tight')

            # contourf = ax.contourf(data['long'].values, data['lat'].values, avgs, levels=levels, cmap=plt.cm.jet)
            # Try different coloring maps such as: plt.cm.viridis
            # @see https://matplotlib.org/tutorials/colors/colormaps.html
            contourf = ax.contourf(lons, lats, avgs, levels=levels, cmap=plt.cm.jet)

            geojson = geojsoncontour.contourf_to_geojson(
                contourf=contourf,
                min_angle_deg=None, #3.0,
                ndigits=None, #3,
                stroke_width=0, #2,
                fill_opacity=0.5
            )

            plt.close(figure)

            name = 'geojsons/{}-weekend-{}-hod-{}.json'.format(parameter, weekend, hod)
            file = open(name, 'w')
            file.write(geojson)
            file.close()
            print('Finished: {}'.format(name))
print('DONE.')