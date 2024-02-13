# Example file for Advanced Python: Hands On by Joe Marini
# Using the reduce function
import pprint
import json
from functools import reduce

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: how much snowfall is in the entire dataset?
total_snowfall = reduce(lambda acc, elem: acc + elem["snow"], weatherdata, 0)
# the lambda functiontakes two arguments:
# acc: the accumulated value
# elem: the current element being processed

# The reduce function takes three parameters:
# the lambda function to call -->take each element and add its value to the accumulator
# the dataset to process --> weatherdata
# the initial value of the accumulator --> 0


pprint.pp(total_snowfall)

# TODO: how much total precipitation is in the entire dataset?
total_precip = reduce(lambda acc, elem: acc + (elem["prcp"] + elem['snow']), weatherdata, 0) # We can sum up different elements in the same reduce function
pprint.pp(total_precip)


# TODO: What was the warmest day in which it snowed? Need to find highest 'tmax' for all
# days where 'snow' > 0

def warm_snow_day(Zwischenspeicher, element):
    # return the elem value if the snow amount > 0 and its tmax value is
    # larger than the tmax value that is in the acc argument
    return element if element["snow"] > 0 and element["tmax"] > Zwischenspeicher["tmax"] else Zwischenspeicher
# return the elem value if the snow amount > 0 and its tmax value is larger than the tmax value that is in the acc argument
# otherwise, return the acc value, because this one will be the highest tmax value then

# define a "zero" value start date for the reduce function to start with
start_val = {
    "date": "1900-01-01",
    "tmin": 0,
    "tmax": 0,
    "prcp": 0.0,
    "snow": 0.0,
    "snwd": 0.0,
    "awnd": 0.0
}

# TODO: reduce the data set to the warmest snow day

result = reduce(warm_snow_day, weatherdata, start_val)
# again the reduce function takes three parameters:
# the algorithm to call --> warm_snow_day, and this is just a simple one
# the dataset to process --> weatherdata
# the initial value of the

print(f'Warmest snow day: {result["date"]} with a temp of {result["tmax"]} degrees and snowfall of {result["snow"]} inches.')

