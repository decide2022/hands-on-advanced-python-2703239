# Example file for Advanced Python: Hands On by Joe Marini
# Count items using a default dictionary

import json
import pprint
from collections import defaultdict

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# The defaultdict collection provides a cleaner way of initializing key values
# TODO: Count the number of data points for each year we have data
    
years = defaultdict(int) # create a defaultdict of type int
for day in weatherdata: # loop over the data
    Schlüssel = day['date'][:4] # Der Schlüssel ist die jeweilige Jahreszahl
    years[Schlüssel] += 1 # add 1 to the value for this key, we don't need to check if the key already exists
# if there isn't already a value assigned to a key in the dicitonary, the default value (integer = 0) is used
pprint.pp(years)


# TODO: defaultdict can use more complex objects, like lists, not only simple types like int

years_months = defaultdict(list) # create a defaultdict of type list
for day in weatherdata: # loop over the data
    Schlüssel = day['date'][:7] # Der Schlüssel ist die jeweilige Jahreszahl
    years_months[Schlüssel].append(day) # add the day to the list for this key
# if there isn't already a value assigned to a key in the dicitonary, the default value (empty list) is used
pprint.pp(len(years_months)) # This will return the number of months in the data set
# each of these months does have his data alongside with it, so it will be callable by the key

# TODO: create a dictionary with year-month keys and lists for each day in the month


# What were the coldest and warmest days of each month?
def warmest_day(month):
    wd = max(month, key=lambda d: d['tmax'])
    return (wd['date'], wd['tmax'])

def coldest_day(month):
    cd = min(month, key=lambda d: d['tmin'])
    return (cd['date'], cd['tmin'])

# TODO: loop over the keys of the dictionary and find each warmest and coldest day
for year_month, daylist in years_months.items(): # set year_month and daylist as variables for each item of years_months while looping
    print(f'Warmest day in {year_month}: {warmest_day(daylist)}') # print a text with the actual value of year_month and the result of the function warmest_day 
    print(f'Coldest day in {year_month}: {coldest_day(daylist)}') # while iterating

