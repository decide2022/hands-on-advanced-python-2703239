# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

import json
from datetime import date, timedelta
from time import strftime





# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: The datetime module converts strings into dates fairly easily
dateobj = date.fromisoformat(weatherdata[0]['date'])
print(f"Date: {dateobj}")

# TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)
print(f"Day of week: {dateobj.weekday()}")

# TODO: what was the warmest weekend day in the dataset?
def is_weekend_day(Tag):
    day = date.fromisoformat(Tag['date']) # cast the date string to a date object
    return (day.weekday() == 5 or day.weekday() == 6) # return only Saturday and Sunday

weekend_days = list(filter(is_weekend_day, weatherdata)) # gib eine Liste aus weatherdata zurück, die nur die Wochenendtage enthält

warmest_day = max(weekend_days, key=lambda Tag: Tag['tmax']) # finde den wärmsten Tag in der Liste weekend_days

print(date.fromisoformat(warmest_day['date']).strftime('%a, %d, %b, %Y'), warmest_day['tmax']) # gib das Datum und die Temperatur des wärmsten Tages aus



# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
coldest_day = min(weatherdata, key=lambda Tag: Tag['tmin'])

# convert the date to a Python date
coldest_date = date.fromisoformat(coldest_day['date'])
print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")

# TODO: Look up the next 7 days
avg_temp = 0.0 # initialize the average temperature
next_date = coldest_date # start with the coldest day

for _ in range(7): # run this loop 7 times
    # add one day to the date
    next_date += timedelta(days=1)
    # find the weather data for the next day
    wetterdaten_iterator = next((Tag for Tag in weatherdata if Tag['date'] == str(next_date)), None) # use the next function to create an iterator and return None, when the iterator is exhausted
    # now add the temperature to the average
    avg_temp += (wetterdaten_iterator['tmax'] + wetterdaten_iterator['tmin']) / 2 # add the average temperature of the next day to the average temperature
avg_temp = avg_temp / 7 # divide the sum of the average temperatures by 7 to get the average temperature of the next 7 days
print(f'The average temperature for the next 7 days is {avg_temp:.2f}')

