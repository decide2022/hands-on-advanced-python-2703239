# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall

# The dataset, on which the filter function is called, has to be mentioned as second argument:-)
snowdays = list(filter(lambda day: day['snow'] > 0.0, weatherdata))
# compare the solution with the count in 'basicdata.py'
print(len(snowdays))

# TODO: pretty-print the resulting data set
# pprint.pp(snowdays, width = 5)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(day):
    # define the summer-months
    summer_months = ['-07-', '-08-']
    # is the month in summer?
    # and did it rain more than one inch?
    if any([month in day['date'] for month in summer_months]) and day['prcp'] >= 1.0:
        return True
    return False

# now build a list out of the dataset filtered by our function
summerraindays = list(filter(is_summer_rain_day, weatherdata))

print(len(summerraindays))

pprint.pp(summerraindays)