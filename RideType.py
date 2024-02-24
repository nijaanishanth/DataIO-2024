import csv
import pandas as pd
import matplotlib.pyplot as plt

jan_bike_data = pd.read_csv('January.csv', usecols = ['rideable_type'])
feb_bike_data = pd.read_csv('February.csv', usecols = ['rideable_type'])
mar_bike_data = pd.read_csv('March.csv', usecols = ['rideable_type'])
apr_bike_data = pd.read_csv('April.csv', usecols = ['rideable_type'])
may_bike_data = pd.read_csv('May.csv', usecols = ['rideable_type'])
jun_bike_data = pd.read_csv('June.csv', usecols = ['rideable_type'])
jul_bike_data = pd.read_csv('July.csv', usecols = ['rideable_type'])
aug_bike_data = pd.read_csv('August.csv', usecols = ['rideable_type'])
sep_bike_data = pd.read_csv('September.csv', usecols = ['rideable_type'])
oct_bike_data = pd.read_csv('October.csv', usecols = ['rideable_type'])
nov_bike_data = pd.read_csv('November.csv', usecols = ['rideable_type'])
dec_bike_data = pd.read_csv('December.csv', usecols = ['rideable_type'])

jan_bike_counts = jan_bike_data['rideable_type'].value_counts()
feb_bike_counts = feb_bike_data['rideable_type'].value_counts()
mar_bike_counts = mar_bike_data['rideable_type'].value_counts()
apr_bike_counts = apr_bike_data['rideable_type'].value_counts()
may_bike_counts = may_bike_data['rideable_type'].value_counts()
jun_bike_counts = jun_bike_data['rideable_type'].value_counts()
jul_bike_counts = jul_bike_data['rideable_type'].value_counts()
aug_bike_counts = aug_bike_data['rideable_type'].value_counts()
sep_bike_counts = sep_bike_data['rideable_type'].value_counts()
oct_bike_counts = oct_bike_data['rideable_type'].value_counts()
nov_bike_counts = nov_bike_data['rideable_type'].value_counts()
dec_bike_counts = dec_bike_data['rideable_type'].value_counts()

member_types = ["member", "casual"]

# Combine counts for all months
combined_counts = pd.concat([jan_bike_counts, feb_bike_counts, mar_bike_counts, apr_bike_counts,may_bike_counts, jun_bike_counts, jul_bike_counts, aug_bike_counts, sep_bike_counts, oct_bike_counts, nov_bike_counts, dec_bike_counts], axis=1)
combined_counts.columns = ['January', 'February', 'March', 'April', 'May','June','July','August','September','October','Novemeber','December']
combined_counts = combined_counts.fillna(0)

# Define member types
bike_types = ["classic_bike", "electric_bike", "docked_bike"]

# Plot the bar graph
combined_counts.T.plot(kind='bar')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Number of Occurrences')
plt.title('Occurrences of Bike Types by Month')

plt.show()



