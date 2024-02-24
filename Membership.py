import csv
import pandas as pd
import matplotlib.pyplot as plt

jan_members_data = pd.read_csv('January.csv', usecols = ['member_casual'])
feb_members_data = pd.read_csv('February.csv', usecols = ['member_casual'])
mar_members_data = pd.read_csv('March.csv', usecols = ['member_casual'])
apr_members_data = pd.read_csv('April.csv', usecols = ['member_casual'])
may_members_data = pd.read_csv('May.csv', usecols = ['member_casual'])
jun_members_data = pd.read_csv('June.csv', usecols = ['member_casual'])
jul_members_data = pd.read_csv('July.csv', usecols = ['member_casual'])
aug_members_data = pd.read_csv('August.csv', usecols = ['member_casual'])
sep_members_data = pd.read_csv('September.csv', usecols = ['member_casual'])
oct_members_data = pd.read_csv('October.csv', usecols = ['member_casual'])
nov_members_data = pd.read_csv('November.csv', usecols = ['member_casual'])
dec_members_data = pd.read_csv('December.csv', usecols = ['member_casual'])

jan_member_counts = jan_members_data['member_casual'].value_counts()
feb_member_counts = feb_members_data['member_casual'].value_counts()
mar_member_counts = mar_members_data['member_casual'].value_counts()
apr_member_counts = apr_members_data['member_casual'].value_counts()
may_member_counts = may_members_data['member_casual'].value_counts()
jun_member_counts = jun_members_data['member_casual'].value_counts()
jul_member_counts = jul_members_data['member_casual'].value_counts()
aug_member_counts = aug_members_data['member_casual'].value_counts()
sep_member_counts = sep_members_data['member_casual'].value_counts()
oct_member_counts = oct_members_data['member_casual'].value_counts()
nov_member_counts = nov_members_data['member_casual'].value_counts()
dec_member_counts = dec_members_data['member_casual'].value_counts()

member_types = ["member", "casual"]

# Combine counts for all months
combined_counts = pd.concat([jan_member_counts, feb_member_counts, mar_member_counts, apr_member_counts,may_member_counts, jun_member_counts, jul_member_counts, aug_member_counts, sep_member_counts, oct_member_counts, nov_member_counts, dec_member_counts], axis=1)
combined_counts.columns = ['January', 'February', 'March', 'April', 'May','June','July','August','September','October','Novemeber','December']
combined_counts = combined_counts.fillna(0)

# Define member types
member_types = ["member", "casual"]

# Plot the bar graph
combined_counts.T.plot(kind='bar')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Number of Occurrences')
plt.title('Occurrences of Member Types by Month')

plt.show()



