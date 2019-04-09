import pandas as pd
from uszipcode import SearchEngine
import math
noon_data = pd.read_csv("noon.csv")
noon_data.drop(noon_data.columns[0], axis=1, inplace=True)

search = SearchEngine(simple_zipcode=False)
zips = []
for i in list(range(len(noon_data))):
    zips.append(search.by_coordinates(noon_data['lat'][i], noon_data['long'][i], radius = 10, returns = 1)[0].to_dict()['zipcode'])

zipspd = pd.Series(zips, name = "zips")
noon_data = noon_data.join(zipspd)
noon_data.rename(columns={'Sufur dioxide':'Sulfur dioxide'}, inplace=True)

#Convert ozone ppm to ug/m3
#1 ppm = 1000 ppb
#1 ppb = 1.96 ug/m3
#Source: https://uk-air.defra.gov.uk/assets/documents/reports/cat06/0502160851_Conversion_Factors_Between_ppb_and.pdf
noon_data['Ozone'] = noon_data['Ozone'].apply(lambda x: x*1000*1.96)

#Convert NO2 ppm to ug/m3
#1 ppm = 1000 ppb
#1 ppb = 1.88 ug/m3
#Source: https://uk-air.defra.gov.uk/assets/documents/reports/cat06/0502160851_Conversion_Factors_Between_ppb_and.pdf
noon_data['Nitrogen dioxide'] = noon_data['Nitrogen dioxide'].apply(lambda x: x*1000*1.88)

#Convert SO2 ppm to ug/m3
#1 ppm = 1000 ppb
#1 ppb = 2.62 ug/m3
#Source: https://uk-air.defra.gov.uk/assets/documents/reports/cat06/0502160851_Conversion_Factors_Between_ppb_and.pdf
noon_data['Sulfur dioxide'] = noon_data['Sulfur dioxide'].apply(lambda x: x*1000*2.62)

health_data = pd.read_csv("Health_byzip.csv", dtype={'zips': object})

#Summarize by Zip Code
data = noon_data.copy()
del data['hod']
del data['lat']
del data['long']

joined = pd.merge(data_grouped, health_data, on='zips', how='outer')
joined.to_csv('joined_zip.csv')
