# importing csv module
import csv
import pandas as pd
import matplotlib.pyplot as plt
import math


from datetime import datetime

def get_hour_from_string(time_string):
    # Parse the input string into a datetime object
    time_format = '%Y-%m-%d %H:%M:%S'
    time_object = datetime.strptime(time_string, time_format)
    
    # Extract the hour component from the datetime object
    hour = time_object.hour
    
    return hour


def haversine_distance(start_lat, start_lng, end_lat, end_lng):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    start_lat = math.radians(start_lat)
    start_lng = math.radians(start_lng)
    end_lat = math.radians(end_lat)
    end_lng = math.radians(end_lng)
    
    # Difference in latitude and longitude
    d_lat = end_lat - start_lat
    d_lng = end_lng - start_lng
    
    # Haversine formula
    a = math.sin(d_lat / 2)**2 + math.cos(start_lat) * math.cos(end_lat) * math.sin(d_lng / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

def count_hours(times):
    peak_hours = {}
    for t in times:
        if t in peak_hours:
            peak_hours[t] += 1
        else:
            peak_hours[t] = 1
    return peak_hours

def avg_list(list):
    sum = 0
    count = 0
    for n in list:
        if (n > 0 and n != "nan"):
            sum = sum + n
            count = count + 1    

    return sum / count

months = ['September', 'October', 'November', 'December', 'January', 'February']

times = []

for month in months:
    filename = month + '.csv'
    df = pd.read_csv(filename)

    stime = df['started_at']

    for t in stime:
        t = get_hour_from_string(t)
        times.append(t)

    sl = df['starting_lat']
    slo = df['starting_lng']
    el = df['ending_lat']
    elo = df['ending_lng']

    d = []
    d.append(haversine_distance(sl, slo, el, elo))

    ## put these numbers into excel to generate a graph
    print(month)
    print("avg distance")
    print(avg_list(d))

## paste these numbers into excel to get a graph
peak = count_hours(times)
peak = sorted(peak.items())
print(peak)
