import json
from datetime import date, timedelta
from time import strftime
from functools import reduce

# build one function for all the code below
def miserable_day():
    # open the sample weather data file and use the json module to load and parse it
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)


    # first we have to define the score for miserable days

    #Score = (Wind + (Regen * 10) + (Höchsttemperatur * 0.8))

    # TODO: find the most miserable day in the dataset
    def score_iterator(acc, elem):
        # return the elem value if the score is larger than the score that is in the acc argument and catch the unsupported operand type error
        try:
            return elem if (elem["awnd"] + (elem["prcp"] * 10) + (elem["tmax"] * 0.8)) > (acc["awnd"] + (acc["prcp"] * 10) + (acc["tmax"] * 0.8)) else acc
        except TypeError:
            return acc
        




    # now, we need to initialize the start value for the reduce function
    start_val = {
        "date": "1900-01-01",
        "tmin": 0,
        "tmax": 0,
        "prcp": 0.0,
        "snow": 0.0,
        "snwd": 0.0,
        "awnd": 0.0
    }


    result = reduce(score_iterator, weatherdata, start_val)

    print(f'The most miserable day was {result["date"]} with a score of {result["awnd"] + (result["prcp"] * 10) + (result["tmax"] * 0.8)}')

miserable_day()

import time
print(f"Script execution time: {time.process_time()} seconds")