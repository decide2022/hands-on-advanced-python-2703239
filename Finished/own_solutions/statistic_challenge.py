

def count_days():
    import json
    import statistics

    # open the sample weather data file and use the json module to load and parse it
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.load(weatherfile)

    def average_temp(Tag):
        return (Tag['tmax'] + Tag['tmin']) / 2
    # Wintermonate
    winters = ["-12-", "-01-", "-02-"]

    # Wintertage
    winter_months = [Tag for Tag in weatherdata if any([month in Tag['date'] for month in winters])]

    # Durchschnittstemperatur aller wintertage
    avg_temps = [average_temp(Tag) for Tag in winter_months]

    # Median der Durchschnitte
    avg_mean = statistics.mean(avg_temps)

    # Ausreißer müssen mindestens 2 Standardabweichungen vom Mittelwert entfernt sein
    outlier_temp = avg_mean + (statistics.stdev(avg_temps) * 2)

    # Welche Tage sind Ausreißer?
    outliers = [Tag for Tag in winter_months if average_temp(Tag) >= outlier_temp]

    # Anzahl der Ausreißer
    return len(outliers)

print(count_days())
