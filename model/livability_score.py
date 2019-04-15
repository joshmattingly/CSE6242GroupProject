###
# Helper method for calculating the Livability Score
# Author: Erin McKeon
###

import pandas as pd
import numpy as np
import math

joined = pd.read_csv("./data/joined_zip.csv", index_col=0, usecols=list(range(1,16)))

#WHO Air Quality Guidelines
#PM2.5 (ug/m3)
AQG_PM2_5 = 10
IT1_PM2_5 = 35
IT2_PM2_5 = 25
IT3_PM2_5 = 15

#PM10 (ug/m3)
AQG_PM10 = 20
IT1_PM10 = 70
IT2_PM10 = 50
IT3_PM10 = 30

#Ozone O3 (ug/m3)
AQG_O3 = 100
IT1_O3 = 160

#SO2 (ug/m3)
AQG_SO2 = 20
IT1_SO2 = 125
IT2_SO2 = 50

#NO2 (ug/m3)
AQG_NO2 = 40

asthma = joined['Asthma'].mean()
asthmaed0 = joined['Asthma ED visits (0-18 years)'].mean()
asthmaed1 = joined['Asthma ED visits (0-4 years)'].mean()
asthmaed2 = joined['Asthma ED Visits (65+ years)'].mean()
resp = joined['Chronic lower respiratory disease deaths'].mean()
heart = joined['Diagnosed heart disease'].mean()
hyper = joined['Hypertension'].mean()
lung = joined['Lung cancer incidence'].mean()
copd = joined['Screened or diagnosed with COPD'].mean()

#Calculation factor weights, based on increment of increased mortality per increase in 5ug/m3
wpm25 = 6 #increase in 5ug/m3 = 6% mortality
wpm10 = 3 #increase in 5ug/m3 = 3% mortality
wo3 = .5 #increase in 5ug/m3 = 0.5% mortality
wso2 = .3 #increase in 5ug/m3 = 0.3% mortality
wno2 = .5 #increase in 5ug/m3 = 0.52% mortality

def livability(zip_code, pm_2_5, pm_10, ozone, no2, so2):
    # CHECK THAT WE HAVE DATA
    exists = np.any(joined.index.isin([int(zip_code)]))
    if not exists:
        # ZIP NOT FOUND - can't return a valid livability score for this
        return -1

    row = joined.loc[int(zip_code)]
    liv = 100

    # PM 2.5
    PM_liv = pm_2_5 / AQG_PM2_5
    liv -= PM_liv * wpm25

    #PM10
    PM1_liv = pm_10 / AQG_PM10
    liv -= PM1_liv * wpm10
    
    #Ozone
    O_liv = ozone  / AQG_O3
    liv -= O_liv * wo3
            
    #Nitrogen Dioxide
    NO2_liv = no2 / AQG_NO2
    liv -= NO2_liv * wno2

    #Sulfur Dioxide
    SO2_liv = so2 / AQG_SO2
    liv -= SO2_liv * wso2

    #Health Data
    #Asthma
    ast = row['Asthma'] / asthma
    liv -= ast
    
    ast1 = row['Asthma ED visits (0-18 years)'] / asthmaed0
    liv -= ast1
        
    ast2 = row['Asthma ED visits (0-4 years)'] / asthmaed1
    liv -= ast2
        
    ast3 = row['Asthma ED Visits (65+ years)'] / asthmaed2
    liv -= ast3
    
    #Chronic lower respiratory disease
    res = row['Chronic lower respiratory disease deaths'] / resp
    liv -= res
    
    #Heart Disease
    hea = row['Diagnosed heart disease'] / heart
    liv -= hea
    
    #Hypertension
    hyp = row['Hypertension'] / hyper
    liv -= hyp
    
    #Lung Cancer Incidence
    lun = row['Lung cancer incidence'] / lung
    liv -= lun
    
    #Screened or diagnosed with COPD
    cop = row['Screened or diagnosed with COPD'] / copd
    liv -= cop

    return max(0, liv)
