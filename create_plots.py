import sys
import code
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt

import data.csse
from plots.cumulative_data import plot_normalized_cumulative_data
from plots.death_rate import plot_normalized_death_rate

plot_normalized_cumulative_data("Confirmed Cases per day", "figures/cases.png", 0.15, ("DE", data.csse.get_cases("Germany")), ("IT", data.csse.get_cases("Italy")), ("US", data.csse.get_cases("US")), ("ES", data.csse.get_cases("Spain")))

plot_normalized_cumulative_data("Deaths per day", "figures/deaths.png", 0.15, ("DE", data.csse.get_deaths("Germany")), ("IT", data.csse.get_deaths("Italy")), ("US", data.csse.get_deaths("US")), ("ES", data.csse.get_deaths("Spain")))

#plot_normalized_death_rate("death_rate", "us", 7, data.csse.get_cases("US"), data.csse.get_deaths("US"))
