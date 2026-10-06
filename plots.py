import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv('air_quality_no2.csv', index_col=0, parse_dates=True)
#air_quality = pd.read_csv('air_quality_no2.csv', index_col=1)

#air_quality.head()
#Step 1-I want a quick visual check of the data.
air_quality.plot()

#Step 2-I want to plot only the columns of the data table with the data from Paris.
air_quality["station_paris"].plot()

#Step 3-I want to visually compare the values measured in London versus Paris.
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

#Step 4-I want to plot only the columns of the data table with the data from London.
air_quality["station_london"].plot()

#Step 4.1
lond=air_quality[["station_london"]]
lond.plot()

#Step 5-  graphical representation showing the median, quartiles, and range of air quality indices
air_quality.plot(kind='box') 
air_quality.plot.box()

plt.show()