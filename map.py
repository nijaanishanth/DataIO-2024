# import csv module
import csv
import pandas as pd
import matplotlib.pyplot as plt
import folium
import webbrowser

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
top_20_stations = total_counts.head(20)

# print
print(top_20_stations)

# Create a map centered at a specific location
mymap = folium.Map(location=[41.881832, -87.623177], zoom_start=10)

# add points to map
# for index, row in data.iterrows():
folium.Marker(location=[41.892278, -87.612043], popup='Streeter Dr & Grand Ave', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.880958, -87.616743], popup='DuSable Lake Shore Dr & Monroe St', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.9009725, -87.623769], popup='Michigan Ave & Oak St', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.911727, -87.626804], popup='DuSable Lake Shore Dr & North Blvd', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.912133, -87.634656], popup='Wells St & Concord Ln', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.902973, -87.63128], popup='Clark St & Elm St', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.8893046666666, -87.6384861666666], popup='Kingsbury St & Kinzie St', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.8810317, -87.62408432], popup='Millennium Park', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.926277, -87.630834], popup='Theater on the Lake', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.9029373333333, -87.6347175], popup='Wells St & Elm St', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.9181961666666, -87.6361766666666], popup='Clark St & Armitage Ave', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.88338, -87.64117], popup='Clinton St & Washington Blvd', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.940107584, -87.652991414], popup='Wilton Ave & Belmont Ave', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.791478, -87.599861], popup='University Ave & 57th St', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.868057251, -87.623009324], popup='Indiana Ave & Roosevelt Rd', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.891466, -87.626761], popup='Wabash Ave & Grand Ave', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.915689, -87.634605], popup='Clark St & Lincoln Ave', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.8827519656856, -87.641201854], popup='Clinton St & Madison St', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.929546, -87.643118], popup='Clark St & Wrightwood Ave', icon=folium.Icon(color='red')).add_to(mymap)
folium.Marker(location=[41.9375823160062, -87.6440978050232], popup='Broadway & Barry Ave', icon=folium.Icon(color='red')).add_to(mymap)

# Display the map
mymap.save("mymap.html")

# Specify the path to your HTML file
html_file_path = "mymap.html"

# Open the generated HTML file in the default web browser
webbrowser.open(html_file_path)
