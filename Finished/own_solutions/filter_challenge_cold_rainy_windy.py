import json
import pprint


def get_cold_windy_rainy_days():

# Open the JSON file
    with open('../../sample-weather-history.json') as weatherfile:
        weatherdata = json.load(weatherfile)


    def is_cold_windy_rainy_day(day):
        # get average temperature
        avg_temp = (day['tmin'] + day['tmax']) / 2
        # get total precipiation
        prec = day['prcp'] + day['snow']
        # place the conditions
        if avg_temp < 45 and prec > 0.7 and day['awnd'] >= 10.0:
            return True
        return False

    blustery_days = list(filter(is_cold_windy_rainy_day, weatherdata))

    return blustery_days

result = get_cold_windy_rainy_days()
print(result)



