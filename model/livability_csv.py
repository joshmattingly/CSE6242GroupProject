###
# Build CSV file for the Livability Score
# Depends On: output_with_zip.csv
###

import pandas as pd
from livability_score import livability

##
# Build the Livability Score for each data point
##
df = pd.read_csv('./data/output_with_zip.csv')

# livability(zip_code, pm_2_5, pm_10, ozone, no2, so2)
def df_livability(row):
    return livability(row['Zip Code'], row['PM 2.5'], row['PM 10'], row['Ozone'], row['Nitrogen dioxide'], row['Sufur dioxide'])
df['Livability'] = df.apply(df_livability, axis=1)

df.to_csv('./data/livability_scores.csv', index=False)
