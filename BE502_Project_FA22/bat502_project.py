# -*- coding: utf-8 -*-
"""bat502_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B9tVz6-nXAsNndBgSQirds-tIHCRasBl
"""

import pandas as pd
import datetime
from datetime import date
import numpy as np
import calendar
import matplotlib.pyplot as plot

#Following code is specific to google notebook
from google.colab import drive 
drive.mount('/content/drive')

copied_path_car ='/content/drive/MyDrive/BAT502_Project/tucson_car_accidents.csv' # copy file path for Car Accidents in Tucson
copied_path_rain = '/content/drive/MyDrive/BAT502_Project/tucson_rain.csv' # copy file path for rain amount in Tucson

#read in data
car_accidents = pd.read_csv(copied_path_car)
rain = pd.read_csv(copied_path_rain, sep=",",header=0)

rain.head()

accidents_aggregate = (car_accidents.groupby(by=['Month', 'Year'],as_index=False)['Hour'].count()
.reindex(columns=car_accidents.columns) )
accidents_aggregate=accidents_aggregate[['Year','Month','Hour']]
accidents_aggregate = accidents_aggregate.set_axis(['Year','Month', 'Number_of_Collisions'], axis=1, inplace=False)
accidents_aggregate.Year=accidents_aggregate.Year.astype('int')

rain['Year']=pd.DatetimeIndex(rain['readingDate']).year
rain['month']=pd.DatetimeIndex(rain['readingDate']).month
rain['Month'] = 0
for i in range(len(rain)):
  rain['Month'][i] = calendar.month_abbr[rain['month'][i]]
rain_aggregate = (rain.groupby(by=['Year', 'Month'],as_index=False)['rainAmount'].mean()
.reindex(columns=rain.columns) )
rain_aggregate = rain_aggregate[['Year', 'Month', 'rainAmount']]
rain_aggregate = rain_aggregate.set_axis(['Year', 'Month', 'rainAmount'], axis=1, inplace=False)
rain_aggregate.Year=rain_aggregate.Year.astype('int')

# rain=rain[rain["createdDate"]<"2018-01-01"]
# rain=rain[rain["quality"].str.upper()=="GOOD"]
# gauges, dates=set(rain["gaugeId"]), list(set(rain["readingDate"])); dates.sort() #add missing zeros and make a gauge, dates matrix
# gauge_rain=pd.DataFrame(np.zeros((len(gauges), len(dates))),index=gauges, columns=dates)
# for i in rain.index:
#     gauge_rain.loc[rain.loc[i,"gaugeId"], rain.loc[i,"readingDate"]] =rain.loc[i, "rainAmount"]
# temp_rain=gauge_rain.reset_index()     # convert the matrix in a (gauge, date) list format
# temp_rain.rename({"index":"gaugeId"},axis=1,inplace=True)
# all_dates=[]
# for col in temp_rain.columns[1:]:
#       curr=temp_rain[["gaugeId",col]]
#       curr.rename({col:"rainAmount"},axis=1,inplace=True)
#       curr["readingDate"]=col
#       all_dates=all_dates+[curr]
# full_rain=pd.concat(all_dates,axis=0,join="inner")
# full_rain=full_rain.reset_index()
# dates=full_rain["readingDate"].str.split("-")
# full_rain["Year"]=[dates[i][0] for i in dates.index]
# full_rain["Month"]=[dates[i][1] for i in dates.index]
# full_rain["Day"]=[dates[i][2] for i in dates.index]
# gauge_info=rain[["gaugeId","lat","lng","gaugeType"]].drop_duplicates()
# full_rain=pd.merge(full_rain,gauge_info,on="gaugeId",how="inner")

# full_rain.head()
# full_rain.shape

rain_aggregate = (rain.groupby(by=['Year', 'Month'],as_index=False)['rainAmount'].mean()
.reindex(columns=rain.columns) )
rain_aggregate = rain_aggregate[['Year', 'Month', 'rainAmount']]
rain_aggregate = rain_aggregate.set_axis(['Year', 'Month', 'rainAmount'], axis=1, inplace=False)
rain_aggregate.Year=rain_aggregate.Year.astype('int')

accidents_aggregate = accidents_aggregate[accidents_aggregate['Year'].isin([2018, 2019, 2020, 2021])]
accidents_aggregate = accidents_aggregate[accidents_aggregate['Month'].isin(['Jun', 'Jul', 'Aug'])]
rain_aggregate = rain_aggregate[rain_aggregate['Year'].isin([2018, 2019, 2020, 2021])]
rain_aggregate = rain_aggregate[rain_aggregate['Month'].isin(['Jun', 'Jul', 'Aug'])]
accidents_aggregate.reset_index(inplace=True)
rain_aggregate.reset_index(inplace=True)

rain_aggregate.shape

df_new = pd.merge(accidents_aggregate, rain_aggregate, on=['Year','Month'], how='inner')

rain_aggregate['monthYear'] = 1
for i in range(len(rain_aggregate)):
  rain_aggregate['monthYear'][i] = str(rain_aggregate['Year'][i]) + ' - ' + str(rain_aggregate['Month'][i])
accidents_aggregate['monthYear'] = 1
for i in range(len(accidents_aggregate)):
  accidents_aggregate['monthYear'][i] = str(accidents_aggregate['Year'][i]) + ' - ' + str(accidents_aggregate['Month'][i])

rain_aggregate.head()

accidents_aggregate.head()

rain_accidents = pd.merge(rain_aggregate, accidents_aggregate, on = ["monthYear"], how = 'inner')
rain_accidents.head(12)

# finding correlation
x = rain_accidents['rainAmount']
y = rain_accidents['Number_of_Collisions']
correlation = np.corrcoef(x,y)[0,1]
value = print("The correlation coefficient  between x and y is :",correlation)

# Scatter plot for Rain Amount

plot.scatter( rain_accidents['monthYear'],rain_accidents['rainAmount'])

plot.title('Plot Rain Amount at a given month/year')

plot.xlabel('Rain Amount')

plot.ylabel('Month and year')

plot.gcf().autofmt_xdate()

plot.show()

# Scatter plot for Number of collisions

plot.scatter( rain_accidents['monthYear'],rain_accidents['Number_of_Collisions'])

plot.title('Plot number of accidents at a given month/year')

plot.xlabel('Number of accidents')

plot.ylabel('Month and year')

plot.gcf().autofmt_xdate()

plot.show()

# Scatter plot for Number of collisions vs Rain Amount
# finding correlation
x = rain_accidents['rainAmount']
y = rain_accidents['Number_of_Collisions']
correlation = np.corrcoef(x,y)[0,1]
value = print("The correlation coefficient  between x and y is :",correlation)

plot.scatter(df_new['rainAmount'], df_new['Number_of_Collisions'])

plot.suptitle('Plot Between Collisions and Rain Amount at a given day')

plot.title(value)

plot.xlabel('Rain Amount')

plot.ylabel('Number of Collisions')
plot.show()