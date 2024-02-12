# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
# initialize a dictionary warmday
# take the dataset weatherdata
# initialize a variable key
# iterate by lambda over all elements of the dataset
# return only the record with the maximum value by max(), depending on the value in 'tmax'
warmday = max(weatherdata, key = lambda x: x['tmax'])

# print the warmest day
# include the key field from the dictionary
print(f"The warmest day was: {warmday['date']} at {warmday['tmax']} degrees Fahrenheit.")
      
# TODO: What was the coldest day in the data set?

coldday = min(weatherdata, key = lambda blub: blub['tmin'])
print(f"The coldest day was: {coldday['date']} at {coldday['tmin']} degrees Fahrenheit.")


# TODO: How many days had snowfall?
# my idea, not the best
# snowfallday = ((weatherdata, key = lambda x: x['snow']) > 0)

# better use list comprehension
snowdays = [bla for bla in weatherdata if bla['snow'] > 0]
print(f"Snow fell on {len(snowdays)} days.")

# Should we believe this?
# Please show the affected records as well

pprint.pp(snowdays)