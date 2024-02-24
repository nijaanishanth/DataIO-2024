import csv
import pandas as pd
import matplotlib.pyplot as plt

jan_members_data = pd.read_csv('January.csv', usecols = ['start_station_name'])
feb_members_data = pd.read_csv('February.csv', usecols = ['start_station_name'])
mar_members_data = pd.read_csv('March.csv', usecols = ['start_station_name'])
apr_members_data = pd.read_csv('April.csv', usecols = ['start_station_name'])
may_members_data = pd.read_csv('May.csv', usecols = ['start_station_name'])
jun_members_data = pd.read_csv('June.csv', usecols = ['start_station_name'])
jul_members_data = pd.read_csv('July.csv', usecols = ['start_station_name'])
aug_members_data = pd.read_csv('August.csv', usecols = ['start_station_name'])
sep_members_data = pd.read_csv('September.csv', usecols = ['start_station_name'])
oct_members_data = pd.read_csv('October.csv', usecols = ['start_station_name'])
nov_members_data = pd.read_csv('November.csv', usecols = ['start_station_name'])
dec_members_data = pd.read_csv('December.csv', usecols = ['start_station_name'])

# Concatenate all data
all_data = pd.concat([jan_members_data, feb_members_data, mar_members_data, apr_members_data,
                      may_members_data, jun_members_data, jul_members_data, aug_members_data,
                      sep_members_data, oct_members_data, nov_members_data, dec_members_data])

# Calculate total counts
total_counts = all_data['start_station_name'].value_counts()

# Select top 10 stations
top_10_stations = total_counts.head(20)

plt.figure(figsize=(8, 8))
plt.pie(top_10_stations, labels=top_10_stations.index, autopct='%1.1f%%', startangle=140)

# Add labels and title
plt.title('Top 20 Rack Stations Occurences')

plt.show()



