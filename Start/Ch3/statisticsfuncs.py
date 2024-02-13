# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# TODO: calculate the mean for both min and max temperatures
max_temps = [Tag['tmax'] for Tag in summer_months]
min_temps = [Tag['tmin'] for Tag in summer_months]
print(f"Mean max temp: {statistics.mean(max_temps)}")
print(f"Mean min temp: {statistics.mean(min_temps)}")


# TODO: calculate the median values for min and max temperatures
print(f'Median max is: {statistics.median(max_temps)}')
print(f'Median min is: {statistics.median(min_temps)}')


# TODO: use the standard deviation function to find outlier temperatures
upper_bound = statistics.mean(max_temps) + (statistics.stdev(max_temps) * 2)
lower_bound = statistics.mean(min_temps) - (statistics.stdev(min_temps) * 2)

print(f"Upper bound: {upper_bound}")
print(f"Lower bound: {lower_bound}")

# TODO: list the outliers
max_outliers = [Tag for Tag in summer_months if Tag['tmax'] >= upper_bound]
min_outliers = [Tag for Tag in summer_months if Tag['tmin'] <= lower_bound]

print(f'Outliers for max: {len(max_outliers)}')
print(f"Max outliers: {max_outliers}")
print(f'Outliers for min: {len(min_outliers)}')
print(f"Min outliers: {min_outliers}")



import time
print(f"Script execution time: {time.process_time()} seconds")