import fileinput
import sys
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

import data.csse
from plots.cumulative_data import plot_normalized_cumulative_data, plot_normalized_cumulative_delta
from plots.average_data import plot_historic_normalized_average_data, plot_historic_normalized_average_delta

def update_date_in_readme():
    for line in fileinput.input("README.md", inplace=1):
        if "Last update" in line:
            print "### Last update: %s" % data.csse.get_days()[-1].strftime("%d.%m.%Y")
        else:
            print line[:-1] # strip the newline character

update_date_in_readme()

case_data = [("DE", data.csse.get_cases("Germany")),
             ("IT", data.csse.get_cases("Italy")),
             ("US", data.csse.get_cases("US")),
             ("ES", data.csse.get_cases("Spain"))]

death_data = [("DE", data.csse.get_deaths("Germany")),
              ("IT", data.csse.get_deaths("Italy")),
              ("US", data.csse.get_deaths("US")),
              ("ES", data.csse.get_deaths("Spain"))]


plot_normalized_cumulative_data("Confirmed Cases", "figures/cases.png",
                                0.15, *case_data)
plot_normalized_cumulative_delta("Daily Confirmed Cases", "figures/daily_cases.png",
                                0.15, *case_data)

plot_normalized_cumulative_data("Deaths", "figures/deaths.png",
                                0.15, *death_data)
plot_normalized_cumulative_delta("Daily Deaths", "figures/daily_deaths.png",
                                0.15, *death_data)

average_days = 7
plot_historic_normalized_average_data(
    "Cases: historic moving average over past %d days" % average_days,
    "figures/cases_historic_average.png", 0.15, average_days,
    *case_data)

plot_historic_normalized_average_data(
    "Deaths: historic moving average over past %d days" % average_days,
    "figures/death_historic_average.png", 0.15, average_days,
    *death_data)

plot_historic_normalized_average_delta(
    "Daily Cases: historic moving average over past %d days" % average_days,
    "figures/daily_cases_historic_average.png", 0.15, average_days,
    *case_data)

plot_historic_normalized_average_delta(
    "Daily Deaths: historic moving average over past %d days" % average_days,
    "figures/daily_death_historic_average.png", 0.15, average_days,
    *death_data)
