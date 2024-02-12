import json
import copy
import pprint

def get_day_temp_descriptions():

    # open the sample weather data file and use the json module to load and parse it
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def average_temp_to_desc(day_data):
        avg_temp = (day_data['tmin'] + day_data['tmax']) / 2
        desc = ''
        if avg_temp <= 60:
            desc = 'cold'
        elif avg_temp > 60 and avg_temp < 80:
            desc = 'warm'
        else:
            desc = 'hot'
        return (day_data['date'], desc)
    
    newdata = list(map(average_temp_to_desc, weatherdata))
    return newdata

result = get_day_temp_descriptions()

pprint.pp(result)


