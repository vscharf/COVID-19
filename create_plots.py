import fileinput
import sys
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

import data.csse
from plots.cumulative_data import plot_normalized_cumulative_data

def update_date_in_readme():
    for line in fileinput.input("README.md", inplace=1):
        if "Last update" in line:
            print "### Last update: %s" % data.csse.get_days()[-1].strftime("%d.%m.%Y")
        else:
            print line[:-1] # strip the newline character

update_date_in_readme()

plot_normalized_cumulative_data("Confirmed Cases per day", "figures/cases.png", 0.15, ("DE", data.csse.get_cases("Germany")), ("IT", data.csse.get_cases("Italy")), ("US", data.csse.get_cases("US")), ("ES", data.csse.get_cases("Spain")))

plot_normalized_cumulative_data("Deaths per day", "figures/deaths.png", 0.15, ("DE", data.csse.get_deaths("Germany")), ("IT", data.csse.get_deaths("Italy")), ("US", data.csse.get_deaths("US")), ("ES", data.csse.get_deaths("Spain")))
